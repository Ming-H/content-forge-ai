#!/bin/bash
# VA Series 下一集自动生成脚本
# 用法: ./scripts/generate_va_next.sh [episode_number]
# 不带参数时自动检测下一集

set -e

cd /Users/z/Documents/work/content-forge-ai
export PYTHONPATH=/Users/z/Documents/work/content-forge-ai

CONFIG_FILE="config/voice_assistant_topics_40.json"
METADATA_FILE="data/series/VA_series/va_series_voice_assistant/series_metadata.json"
LOG_DIR="logs/va_series"
mkdir -p "$LOG_DIR"

# 查找下一集
find_next_episode() {
    python3 -c "
import json
d = json.load(open('$METADATA_FILE'))
for t in d['topics']:
    if t.get('status') != 'completed':
        print(t['episode'])
        break
else:
    print('DONE')
"
}

if [ -z "$1" ]; then
    EPISODE=$(find_next_episode)
else
    EPISODE=$1
fi

if [ "$EPISODE" = "DONE" ]; then
    echo "✅ VA系列全部40集已完成!"
    exit 0
fi

echo "🎯 生成 VA 系列 EP$(printf '%03d' $EPISODE)..."
echo "   开始时间: $(date '+%Y-%m-%d %H:%M:%S')"

LOG_FILE="$LOG_DIR/ep$(printf '%03d' $EPISODE)_$(date +%Y%m%d_%H%M%S).log"

# 运行生成
python3 src/main.py --mode series --episode "$EPISODE" --series-config "$CONFIG_FILE" 2>&1 | tee "$LOG_FILE"
EXIT_CODE=${PIPESTATUS[0]}

if [ $EXIT_CODE -eq 0 ]; then
    # 验证文章是否生成
    EP_DIR="data/series/VA_series/va_series_voice_assistant/episode_$(printf '%03d' $EPISODE)"
    ARTICLE="$EP_DIR/longform/article.md"
    if [ -f "$ARTICLE" ]; then
        WORDS=$(wc -m < "$ARTICLE")
        echo "✅ EP$(printf '%03d' $EPISODE) 完成! 字数: $WORDS"
        echo "   结束时间: $(date '+%Y-%m-%d %H:%M:%S')"
    else
        echo "⚠️ EP$(printf '%03d' $EPISODE) 进程成功但未找到文章文件"
        exit 1
    fi
else
    echo "❌ EP$(printf '%03d' $EPISODE) 生成失败 (exit code: $EXIT_CODE)"
    echo "   日志: $LOG_FILE"
    exit $EXIT_CODE
fi
