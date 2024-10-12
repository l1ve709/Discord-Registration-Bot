import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Modal, TextInput
from datetime import datetime, timezone, timedelta
import logging
import pytz
import asyncio
import pytz
import logging
import sqlite3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

current_time = datetime.now(timezone.utc)
print("UTC Zamanı:", current_time)

tz = pytz.timezone('Europe/Istanbul')
tarih = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
print("Türkiye Zamanı:", tarih)


intents = discord.Intents.all()
l1ve709 = commands.Bot(command_prefix='.', intents=intents)
kayıtkanalid = 1272221108313264222  # ! REGİSTER CHANEL  / KAYIT YAPILAN KANAL
üyerolüid = 1189271113998532718  # ! MEMBER ROLE / ÜYE ROLÜ
kayıtçırolüid = [1247644798782017576] # ! REGİSTİON STAFF ROLE  / KAYITÇI ROLÜ
kayıtlog = 1248208121713786923  # REGİSTER LOG / KAYIT GÜNLÜĞÜ
kayıtsızrolüid = 1189271113130319953 #! DONT REGİSTER ROLE / KAYITSIZ KİŞİ ROLÜ
kayıtçı = 1247644798782017576  # REGİSTİRİON STAFF ROLE / KAYITÇI ROLÜ

kayit_durumu = {}
kayit_sayilari = {}

class KayitFormu(Modal):
    def __init__(self, üye):
        super().__init__(title="Kayıt Formu")
        self.üye = üye

        self.roblox_isim = TextInput(label="Roblox İsmi", placeholder="Örnek: user123")
        self.ic_isim = TextInput(label="IC İsmi", placeholder="Örnek: Ediz")
        self.roblox_link = TextInput(label="Roblox Profil Linki", placeholder="Örnek: https://roblox.com/user-id")
        self.karakter_hikayesi = TextInput(
            label="Karakter Hikayesi", 
            placeholder="Karakterinizin hikayesini buraya yazın.", 
            style=discord.TextStyle.paragraph, 
            max_length=500  
        )

        self.add_item(self.roblox_isim)
        self.add_item(self.ic_isim)
        self.add_item(self.roblox_link)
        self.add_item(self.karakter_hikayesi)

    async def on_submit(self, interaction: discord.Interaction):
        await kayit_et(
            interaction.user, 
            self.üye, 
            self.roblox_isim.value, 
            self.ic_isim.value, 
            self.roblox_link.value, 
            self.karakter_hikayesi.value,
            interaction
        )



@l1ve709.event
async def on_ready():
    await l1ve709.tree.sync()  
    logger.info(f"{l1ve709.user}")


@l1ve709.event
async def on_member_join(member):
    try:
        kayitsiz_rolu_obj = member.guild.get_role(kayıtsızrolüid)
        if kayitsiz_rolu_obj is None:
            logger.error(f"Kayıtsız rolü bulunamadı: {kayıtsızrolüid}")
            return
        
        await member.add_roles(kayitsiz_rolu_obj)

        kayit_durumu[member.id] = {
            'join_time': datetime.now(timezone.utc),
            'registered': False
        }

        kayit_kanali_obj = l1ve709.get_channel(kayıtkanalid)
        await hosgeldin_mesaji(member, l1ve709, kayit_kanali_obj)

    except Exception as e:
        logger.error(f"Üye katılırken hata: {str(e)}")

async def hosgeldin_mesaji(member, l1ve709, kayit_kanali_obj):
    hesap_olusturulma = (member.created_at + timedelta(hours=3)).strftime("%d/%m/%Y %H:%M") if member.created_at else "Bilinmiyor"
    katilma_tarihi = (member.joined_at + timedelta(hours=3)).strftime("%d/%m/%Y %H:%M") if member.joined_at else "Bilinmiyor"    
    etiketleme_mesaji = f"{member.mention} sunucumuza hoş geldin!"
    await kayit_kanali_obj.send(etiketleme_mesaji)

    mesaj = (
        f"Hesap oluşturulma tarihi: `{hesap_olusturulma}`\n"
        f"Sunucuya katılma tarihi: `{katilma_tarihi}`\n\n"
        f"Seninle birlikte **{len(member.guild.members)}** kişiyiz.\n\n"
        f"Kayıt olmak istiyorsan herhangi bir mülakat kanalına geçiş yaparsan <@&{kayıtçı}> en kısa sürede seninle ilgilenecektir!"
    )
    
    await kayit_kanali_obj.send(mesaj)

    await asyncio.sleep(300)  
    if not kayit_durumu.get(member.id, {}).get('registered', False):
        try:
            await member.send("Lütfen sunucuya girip kayıt olunuz! discord.gg/adanarp")
        except discord.Forbidden:
            logger.warning(f"{member} kullanıcısına DM gönderilemedi.")



async def kayit_et(kayitci, üye, roblox_isim, ic_isim, roblox_link, karakter_hikayesi, ctx_or_interaction):
    if üye.id not in kayit_durumu:
        kayit_durumu[üye.id] = {'registered': False}

    try:
        yeni_nick = f"{ic_isim} | (@{roblox_isim})"
        await üye.edit(nick=yeni_nick)

        kayitsiz_rolu_obj = üye.guild.get_role(kayıtsızrolüid)
        if kayitsiz_rolu_obj is None:
            logger.error(f"Kayıtsız rolü bulunamadı: {kayıtsızrolüid}")
            return

        await üye.remove_roles(kayitsiz_rolu_obj)
        await üye.add_roles(discord.Object(id=üyerolüid))

        kayit_durumu[üye.id]['registered'] = True

        if kayitci.id not in kayit_sayilari:
            kayit_sayilari[kayitci.id] = 0
        kayit_sayilari[kayitci.id] += 1

        embed = discord.Embed(
            title="✅ Kayıt Yapıldı!",
            description=(
                f"Kayıt Bilgileri:\n"
                f"**Roblox İsmi:** {roblox_isim}\n"
                f"**IC İsmi:** {ic_isim}\n"
                f"**Roblox Linki:** [Profil Linki]({roblox_link})\n"
                f"**Karakter Hikayesi:** {karakter_hikayesi}\n"
                f"**Kayıt Eden Kullanıcı:** {kayitci.mention}\n"
                f"**Kayıt Edilen Kullanıcı:** {üye.mention}\n" 
            ),
            color=discord.Color.green()
        )

        if üye.guild.icon:
            embed.set_author(name=üye.guild.name, icon_url=üye.guild.icon.url)

        embed.set_thumbnail(url=üye.avatar.url)
        embed.set_footer(text=l1ve709.user.name, icon_url=l1ve709.user.avatar.url)

        if isinstance(ctx_or_interaction, discord.Interaction):
            await ctx_or_interaction.response.send_message(embed=embed)
        else:
            await ctx_or_interaction.send(embed=embed)

        ekstra_kanal_obj = üye.guild.get_channel(kayıtlog)
        if ekstra_kanal_obj:
            ekstra_embed = discord.Embed(
                title="📋 Kayıt Log",
                description=(
                    f"**Kayıt edilen kullanıcı:** {üye.mention}\n\n"  
                    f"**Roblox İsmi:** {roblox_isim}\n"
                    f"**IC İsmi:** {ic_isim}\n"
                    f"**Roblox Linki:** [Profil Linki]({roblox_link})\n"
                    f"**Kayıt Eden:** {kayitci.mention}\n"
                    f"**Karakter Hikayesi:** {karakter_hikayesi}\n"  
                ),
                color=discord.Color.dark_gray()
            )

            ekstra_embed.set_thumbnail(url=üye.avatar.url)
            await ekstra_kanal_obj.send(embed=ekstra_embed)
        else:
            logger.error(f"Ekstra kanal bulunamadı: {kayıtlog}")

    except discord.errors.Forbidden as e:
        logger.error(f"Yetki hatası: {str(e)}")
        if isinstance(ctx_or_interaction, discord.Interaction):
            await ctx_or_interaction.response.send_message("Botun gerekli yetkileri yok. Lütfen yetkilerini kontrol edin.", ephemeral=True)
        else:
            await ctx_or_interaction.send("Botun gerekli yetkileri yok. Lütfen yetkilerini kontrol edin.", ephemeral=True)
    except Exception as e:
        logger.error(f"Kayıt sırasında hata: {str(e)}")
        if isinstance(ctx_or_interaction, discord.Interaction):
            await ctx_or_interaction.response.send_message("Kayıt sırasında bir hata oluştu.", ephemeral=True)
        else:
            await ctx_or_interaction.send("Kayıt sırasında bir hata oluştu.", ephemeral=True)




@l1ve709.tree.command(name="kayıt", description="Bir kullanıcıyı sunucu kayıt et.")
@app_commands.describe(üye="Kayıt edilecek üye", roblox_isim="Roblox kullanıcı adı", ic_isim="IC ismi", roblox_link="Roblox profil linki", karakter_hikayesi="Karakter hikayesi")
async def kayit(interaction: discord.Interaction, üye: discord.Member, roblox_isim: str, ic_isim: str, roblox_link: str, karakter_hikayesi: str):
    x12 = [1235388304200040579, 1247644798782017576] # kullanamaya yetkisi olan roller 
    
    if not any(role.id in x12 for role in interaction.user.roles):
        await interaction.response.send_message("Bu komutu kullanmak için gerekli role sahip değilsiniz.", ephemeral=True)
        return
    
    await kayit_et(interaction.user, üye, roblox_isim, ic_isim, roblox_link, karakter_hikayesi, interaction)

async def kayit_et(kayitci, üye, roblox_isim, ic_isim, roblox_link, karakter_hikayesi, ctx_or_interaction):
    if üye.id not in kayit_durumu:
        kayit_durumu[üye.id] = {'registered': False}
    
    try:
        yeni_nick = f"{ic_isim} | (@{roblox_isim})"
        await üye.edit(nick=yeni_nick)

        kayitsiz_rolu_obj = üye.guild.get_role(kayıtsızrolüid)
        if kayitsiz_rolu_obj is None:
            logger.error(f"Kayıtsız rolü bulunamadı: {kayıtsızrolüid}")
            return

        await üye.remove_roles(kayitsiz_rolu_obj)
        await üye.add_roles(discord.Object(id=üyerolüid))

        kayit_durumu[üye.id]['registered'] = True

        if kayitci.id not in kayit_sayilari:
            kayit_sayilari[kayitci.id] = 0
        kayit_sayilari[kayitci.id] += 1

        embed = discord.Embed(
            title="✅ Kayıt Yapıldı!",
            description=(
                f"Kayıt Bilgileri:\n"
                f"**Roblox İsmi:** {roblox_isim}\n"
                f"**IC İsmi:** {ic_isim}\n"
                f"**Roblox Linki:** [Profil Linki]({roblox_link})\n"
                f"**Karakter Hikayesi:** {karakter_hikayesi}\n"
                f"**Kayıt Eden Kullanıcı:** {kayitci.mention}\n"
            ),
            color=discord.Color.green()
        )

        if üye.guild.icon:
            embed.set_author(name=üye.guild.name, icon_url=üye.guild.icon.url)

        embed.set_thumbnail(url=üye.avatar.url)
        embed.set_footer(text=l1ve709.user.name, icon_url=l1ve709.user.avatar.url)

        if isinstance(ctx_or_interaction, discord.Interaction):
            await ctx_or_interaction.response.send_message(embed=embed)
        else:
            await ctx_or_interaction.send(embed=embed)

        ekstra_kanal_obj = üye.guild.get_channel(kayıtlog)
        if ekstra_kanal_obj:
            ekstra_embed = discord.Embed(
                title="📋 Kayıt Log",
                description=(
                    f"**Kayıt edilen kullanıcı:** {üye.mention}\n\n"  
                    f"**Roblox İsmi:** {roblox_isim}\n"
                    f"**IC İsmi:** {ic_isim}\n"
                    f"**Roblox Linki:** [Profil Linki]({roblox_link})\n"
                    f"**Kayıt Eden:** {kayitci.mention}\n"
                    f"**Karakter Hikayesi:** {karakter_hikayesi}\n"  
                ),
                color=discord.Color.dark_gray()
            )

            ekstra_embed.set_thumbnail(url=üye.avatar.url)
            await ekstra_kanal_obj.send(embed=ekstra_embed)
        else:
            logger.error(f"Ekstra kanal bulunamadı: {kayıtlog}")

    except Exception as e:
        logger.error(f"Kayıt sırasında hata: {str(e)}")
        await ctx_or_interaction.send("Kayıt sırasında bir hata oluştu.", ephemeral=True)


SQLALLAHPORO = 'kayıt_info.db'

def veritabani_baglan():
    return sqlite3.connect(SQLALLAHPORO)

def veritabani_olustur():
    with veritabani_baglan() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS kayit_sayilari (
            member_id INTEGER PRIMARY KEY,
            kayit_sayi INTEGER DEFAULT 0
        )
        ''')
        conn.commit()

def kayit_sayisi_guncelle(member_id, kayit_sayi=1):
    with veritabani_baglan() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM kayit_sayilari WHERE member_id = ?', (member_id,))
        result = cursor.fetchone()
        if result:
            cursor.execute('UPDATE kayit_sayilari SET kayit_sayi = kayit_sayi + ? WHERE member_id = ?', (kayit_sayi, member_id))
        else:
            cursor.execute('INSERT INTO kayit_sayilari (member_id, kayit_sayi) VALUES (?, ?)', (member_id, kayit_sayi))
        conn.commit()

def kayitlari_getir():
    with veritabani_baglan() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM kayit_sayilari')
        return cursor.fetchall()

yetkili_idleri = [794909914760871967, 690646689811398676, 1235388304200040579, 1247644798782017576]  

veritabani_olustur()

@l1ve709.tree.command(name="kayıtsayı", description="Yetkililerin kayıt sayılarını görüntüler.")
async def kayitsayisi(interaction: discord.Interaction):
    kayitlar = kayitlari_getir()

    embed = discord.Embed(
        title="Yetkililerin Kayıt Sayıları",
        description="Aşağıda tüm yetkililerin kayıt sayıları bulunmaktadır:"
    )

    for member_id, kayit_sayi in kayitlar:
        member = interaction.guild.get_member(member_id)
        if member:  
            embed.add_field(name=str(member), value=f"**{kayit_sayi}** kayıt", inline=True)

    if not embed.fields:
        embed.add_field(name="Bilgi", value="Henüz kayıt yapılmamış.", inline=False)

    await interaction.response.send_message(embed=embed)



l1ve709.run("your discord token paste here")
