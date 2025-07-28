# 🎉 LINE Birthday Reminder Bot

這是一個透過 GitHub Actions 定時執行的生日提醒機器人，會自動向指定的 LINE 使用者推送生日祝福訊息。

## 🔧 使用方式

1. 建立 GitHub Repository。
2. 加入 Secrets：
   - `LINE_CHANNEL_ACCESS_TOKEN`: 你的 LINE Channel Token
   - `BIRTHDAY_JSON`: 例如：
     ```json
     {
       "Alice": {
         "userId": "Uxxxxxxxxxxxxxxxxxxxx",
         "date": "07-28"
       }
     }
     ```
3. 修改 `.github/workflows/birthday_reminder.yml` 內的時間（UTC）。
4. 完成後 GitHub Actions 每天自動提醒 🎂
