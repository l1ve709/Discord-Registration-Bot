
## Sunucu Kayıt Botu (ROLEPLAY SUNUCULARI İÇİN BİREBİR)

Bu bot, Discord sunucuları için kullanıcı kayıt sistemi sağlar. Üyeler, sunucuya katıldıklarında kayıt ekibi tarafından mülakata alınabilir ve gerekli bilgiler toplanarak sunucuda kayıt altına alınabilirler. Ayrıca, kayıt işlemiyle ilgili çeşitli loglar tutulur ve yetkililerin kayıt sayıları takip edilir.

## Kullanılan Dil(ler) ve Kütüphane(ler)

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py,sqlite">
</picture>
discord.py, pytz, datetime, asyncio, logging

### Özellikler

1. **Kayıtsız Rol Atama:** Sunucuya yeni katılan üyelere otomatik olarak `kayıtsız` rolü atanır.
2. **Hoş Geldin Mesajı:** Yeni üyeye özel mesaj olarak hoş geldin mesajı gönderilir ve sunucuya nasıl kayıt olunacağı hakkında bilgilendirilir.
3. **Kayıt Formu:** Bir üyenin kaydedilmesi için, kayıt formu oluşturulur ve bu formda üyeden aşağıdaki bilgiler istenir:
   - Roblox İsmi
   - IC (In Character) İsmi
   - Roblox Profil Linki
   - Karakter Hikayesi
4. **Kayıt Sistemi:** Kayıt işlemi başarıyla tamamlandığında, kullanıcının sunucuya kayıt edildiği bilgisi loglanır ve kayıt işlemi gerçekleştirilir.
5. **Yetkililerin Kayıt Sayısı:** Kayıt işlemlerini yapan yetkililerin kaç kişiyi kayıt ettiği, bir komut ile görüntülenebilir.
6. **Veritabanı:** Kayıt sayıları, SQLite veritabanında saklanır ve gerektiğinde sorgulanabilir.

### Gereksinimler

- Python 3.8+
- Discord.py 2.0 veya üzeri
- `pytz`, `sqlite3`, `logging`, `asyncio`  kütüphaneler,i

### Kurulum Adımları

1. **Python ve Kütüphanelerin Yüklenmesi:**
   ```bash
   pip install discord.py pytz
   ```

2. **Botun Çalıştırılması:**
   - Discord geliştirici portalından bir bot oluşturun ve gerekli izinleri verin.
   - `bot.run("your discord token paste here")` satırına kendi Discord bot tokenınızı yapıştırın.
   - Botu çalıştırmak için terminalde şu komutu kullanın:
     ```bash
     python bot.py
     ```

3. **Veritabanı Kurulumu:**
   Bot çalıştığında, SQLite veritabanı otomatik olarak oluşturulur ve gerekli tablolar kurulur.

### Komutlar

1. **/kayıt**
   - Açıklama: Bir kullanıcıyı sunucuya kaydeder.
   - Kullanımı: `/kayıt @kullanıcı roblox_isim ic_isim roblox_link karakter_hikayesi`
   - Yetki: Belirtilen `kayıtçı` rollerine sahip kullanıcılar kullanabilir.

2. **/kayıtsayı**
   - Açıklama: Yetkililerin kayıt sayılarını gösterir.
   - Kullanımı: `/kayıtsayı`
   - Yetki: Kayıt komutunu kullanabilen kişiler görüntüleyebilir.

### Loglama

- Kayıt işlemleri ve bot etkinlikleri, Python `logging` modülü aracılığıyla loglanır. Hatalar ve önemli olaylar konsolda gösterilir.

### Özelleştirme

- **ID'ler:** Sunucuya özel `rol`, `kanal` ve `yetkili` ID'lerini kendi sunucunuzun ID'leriyle değiştirin.
- **Bot Prefix:** Varsayılan komut prefix'i `.` olarak ayarlanmıştır. Bunu `commands.Bot(command_prefix='.')` satırından değiştirebilirsiniz.

### Sorun Giderme

- **Bot Çalışmıyorsa:** Discord tokenınızı kontrol edin ve doğru izinleri verdiğinizden emin olun.
- **Rol/İzin Hataları:** Botun gerekli yetkilere sahip olduğundan ve doğru rollerin ID'lerinin ayarlandığından emin olun.

### Geliştirici Bilgileri

Bu bot, sunucu içi kayıt süreçlerini hızlandırmak ve kayıt loglarını tutmak amacıyla geliştirilmiştir. Botun işlevselliğini genişletmek için Discord.py 2.0 ve üzerinde kullanılan yeni uygulama komutları (application commands) kullanılmıştır.

---

Eğer hatayla karşılaşırsanız benle iletişime geçin: githubsupport@l1ve709.com / instagram: l1ve709


## Discord Hesabım
![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)
