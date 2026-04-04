#!/bin/bash
# VA Series 连续生成脚本
# 自动检测进度，从下一集开始连续生成到结束
# 用法: ./scripts/generate_va_all.sh [start_episode] [end_episode]

cd /Users/z/Documents/work/content-forge-ai
export PYTHONPATH=/Users/z/Documents/work/content-forge-ai

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG_FILE="config/voice_assistant_topics_40.json"
METADATA_FILE="data/series/VA_series/va_series_voice_assistant/series_metadata.json"
LOG_DIR="logs/va_series"
mkdir -p "$LOG_DIR"

TOTAL_LOG="$LOG_DIR/batch_$(date +%Y%m%d_%H%M%S).log"

echo "========================================" | tee -a "$TOTAL_LOG"
echo "VA Series 批量生成" | tee -a "$TOTAL_LOG"
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$TOTAL_LOG"
echo "========================================" | tee -a "$TOTAL_LOG"

SUCCESS=0
FAIL=0
FAIL_LIST=""

generate_episode() {
    local EP=$1
    local EP_DIR="data/series/VA_series/va_series_voice_assistant/episode_$(printf '%03d' $EP)"
    local ARTICLE="$EP_DIR/longform/article.md"

    # 跳过已完成的集
    if [ -f "$ARTICLE" ]; then
        echo "⏭️ EP$(printf '%03d' $EP) 已存在，跳过" | tee -a "$TOTAL_LOG"
        return 0
    fi

    echo "" | tee -a "$TOTAL_LOG"
    echo "🎯 [$(date '+%H:%M:%S')] 开始生成 EP$(printf '%03d' $EP)..." | tee -a "$TOTAL_LOG"

    local EP_LOG="$LOG_DIR/ep$(printf '%03d' $EP)_$(date +%Y%m%d_%H%M%S).log"
    local START_TIME=$(date +%s)

    python3 src/main.py --mode series --episode "$EP" --series-config "$CONFIG_FILE" > "$EP_LOG" 2>&1
    local EXIT_CODE=$?

    local END_TIME=$(date +%s)
    local DURATION=$(( (END_TIME - START_TIME) / 60 ))

    if [ $EXIT_CODE -eq 0 ] && [ -f "$ARTICLE" ]; then
        local WORDS=$(wc -m < "$ARTICLE")
        echo "✅ EP$(printf '%03d' $EP) 完成 | 字数: $WORDS | 耗时: ${DURATION}min" | tee -a "$TOTAL_LOG"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "❌ EP$(printf '%03d' $EP) 失败 (exit: $EXIT_CODE, 耗时: ${DURATION}min)" | tee -a "$TOTAL_LOG"
        echo "   日志: $EP_LOG" | tee -a "$TOTAL_LOG"
        FAIL=$((FAIL + 1))
        FAIL_LIST="$FAIL_LIST $EP"

        # 连续失败3次则停止
        if [ $FAIL -ge 3 ]; then
            echo "⛔ 连续失败3次，停止生成" | tee -a "$TOTAL_LOG"
            return 1
        fi
    fi

    return 0
}

# 确定范围
START_EP=${1:-0}  # 0 means auto-detect
END_EP=${2:-40}

if [ "$START_EP" -eq 0 ]; then
    # 自动检测下一集
    START_EP=$(python3 -c "
import json
d = json.load(open('$METADATA_FILE'))
for t in d['topics']:
    if t.get('status') != 'completed':
        print(t['episode'])
        break
else:
    print(99)
" 2>/dev/null || echo 7)
fi

echo "生成范围: EP$(printf '%03d' $START_EP) ~ EP$(printf '%03d' $END_EP)" | tee -a "$TOTAL_LOG"
echo "" | tee -a "$TOTAL_LOG"

# 循环生成
for EP in $(seq $START_EP $END_EP); do
    generate_episode $EP || break
    # 集间短暂休息，避免API限流
    sleep 5
done

echo "" | tee -a "$TOTAL_LOG"
echo "========================================" | tee -a "$TOTAL_LOG"
echo "📊 汇总: 成功 $SUCCESS | 失败 $FAIL" | tee -a "$TOTAL_LOG"
[ -n "$FAIL_LIST" ] && echo "   失败集数:$FAIL_LIST" | tee -a "$TOTAL_LOG"
echo "结束时间: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$TOTAL_LOG"
echo "========================================" | tee -a "$TOTAL_LOG"
