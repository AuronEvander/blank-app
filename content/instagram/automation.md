# Instagram düzeneği: nasıl otomatik paylaşırız

Hedef: `posts.json` içindeki paylaşımların her Pzt/Çar/Cum 10:00'da (TR) otomatik gitmesi.

## 1. Bağlantı (bir kez, elle)
1. Instagram hesabını **Instagram Business/Creator** yapın ve bir Facebook Sayfası'na bağlayın.
2. Windsor.ai üzerinden `instagram` bağlayıcısını yetkilendirin (Claude'daki Windsor connector
   şu an yalnızca Meta Ads, Google Ads, GA4 ve Search Console hesaplarını görüyor; Instagram
   henüz bağlı değil).
3. Görseller herkese açık bir HTTPS adreste olmalı: `site/` GitHub Pages'e çıktığında
   `https://<kullanıcı>.github.io/blank-app/assets/...` adresleri kullanılabilir.

## 2. Zamanlayıcı (Claude Routine)
Bağlantı tamamlanınca Claude'da haftalık bir Routine kurulur:
- Cron: `0 7 * * 1,3,5` (UTC; İstanbul 10:00)
- Görev: `content/instagram/posts.json` içinden `status: "scheduled"` olan ilk kaydı al,
  Windsor `instagram.create_image_post` ile paylaş, kaydı `posted` yap ve commit'le.
- Paylaşımdan önce onay istenirse: Routine yalnızca taslağı hazırlar, kullanıcı "gönder" der.

## 3. İçerik üretimi
- Görseller: Higgsfield `gpt_image_2_5` (referans: `site/assets/step5_prototype.jpg`), 1:1 veya 4:5.
- Reels: Higgsfield `kling3_0` (pro, 8 sn, 9:16) başlangıç karesi olarak üretilen görsel.
- Açıklamalar: `posts.json` içindeki TR/EN metinler; hashtag seti `calendar.md`'de.
