# Social Automation Hub

منصة Userscript متعددة المنصات لإدارة النشر من واجهة موحدة.

## الإصدار الأول v0.1.0

المنصات العاملة حالياً:

- Bluesky: نشر نص وصورة + اختبار الاتصال + جدولة نصية.
- Facebook Pages: نشر نص وصورة وفيديو عبر Graph API + اختبار الاتصال + جدولة نصية.

المنصات الظاهرة في الواجهة كملفات مستقلة وجاهزة للتطوير لاحقاً:

YouTube, TikTok, Kick, Twitch, Discord, Instagram, Threads, Pinterest, Kwai, X, WhatsApp, GitHub, Telegram.

## هيكل المشروع

```text
social-automation-hub/
├─ userscript.meta.js
├─ build.py
├─ src/
│  ├─ core.js
│  ├─ ui.js
│  ├─ main.js
│  └─ connectors/
│     ├─ facebook.js
│     ├─ bluesky.js
│     ├─ youtube.js
│     ├─ tiktok.js
│     ├─ kick.js
│     ├─ twitch.js
│     ├─ discord.js
│     ├─ instagram.js
│     ├─ threads.js
│     ├─ pinterest.js
│     ├─ kwai.js
│     ├─ x.js
│     ├─ whatsapp.js
│     ├─ github.js
│     └─ telegram.js
└─ dist/
   └─ social-hub.user.js
```

## تثبيت مباشر

استخدم الملف:

```text
dist/social-hub.user.js
```

في Tampermonkey.

## Bluesky

من إعداد المنصة أدخل:

- Handle مثل `username.bsky.social`
- App Password من إعدادات Bluesky

يتم حفظ السر مشفراً في تخزين Tampermonkey وليس في DOM.

## Facebook

التكامل الحالي مخصص **لصفحات Facebook Pages** عبر Graph API. الملف الشخصي العادي لا يدعم نفس أسلوب النشر الآلي بواسطة Pages API.

تحتاج:

- Facebook Page ID
- Page Access Token بصلاحيات النشر المناسبة لتطبيق Meta الخاص بك
- Graph API Version (الافتراضي في المشروع `v26.0`)

> لا تضع App Secret داخل Userscript ولا ترفعه إلى GitHub.

## الأمان

- الأسرار مشفرة محلياً بـ AES-GCM.
- مفتاح التشفير محفوظ في GM storage الخاص بمدير Userscripts بدلاً من LocalStorage الخاص بالموقع.
- حقول كلمات المرور لا يعاد ملؤها في DOM.
- لا يوجد App Secret داخل الكود.
- لا يمكن ضمان خلو أي برنامج من الثغرات بشكل مطلق؛ راجع الصلاحيات والتوكنات قبل استخدام المشروع في حسابات مهمة.

## الجدولة

v0.1.0 تدعم جدولة المنشورات النصية. الوسائط المجدولة لم تُفعّل بعد لأن File objects لا ينبغي تخزينها بهذه الطريقة في الإعدادات المحلية؛ ستحتاج Media Store منفصلاً في إصدار لاحق.

## الاختصار

`Shift + S` لإظهار أو إخفاء Social Hub.

## البناء

```bash
python build.py
```

ثم سيُنشأ:

```text
dist/social-hub.user.js
```
