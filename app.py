import streamlit as st
import random

# --- UYGULAMA AYARLARI ---
st.set_page_config(page_title="Viral Script Master", page_icon="🚀")

st.title("🚀 Viral Script Master AI")
st.subheader("İzlenme Garantili Video Senaryosu Oluşturucu")
st.write("Konunu yaz, saniyeler içinde milyonluk kanca (hook) ve senaryonu al.")

# --- KULLANICI GİRİŞİ ---
topic = st.text_input("Videonun Konusu Nedir?", placeholder="Örn: Evde spor yapmak, Dropshipping, İngilizce öğrenmek...")
tone = st.selectbox("Video Tonu", ["Eğlenceli & Hızlı", "Gizemli & Merak Uyandırıcı", "Sert Gerçekler & Uyarıcı"])

# --- VIRAL FORMÜL MOTORU (ARKA PLAN) ---
def generate_script(topic, tone):
    # Gerçek bir uygulamada buraya OpenAI API bağlanır.
    # Şimdilik "Viral Formülleri" simüle ediyoruz.
    
    hooks = [
        f"Sakın {topic} hakkında bu hatayı yapmayın! 🛑",
        f"Kimse size {topic} konusundaki bu sırrı anlatmıyor... 🤫",
        f"30 saniyede {topic} problemini sonsuza kadar çözün. ⏱️",
        f"Eğer {topic} ile ilgileniyorsanız, bunu izlemek zorundasınız."
    ]
    
    body = [
        f"Çoğu insan {topic} yaparken yanlış yoldan gidiyor. Asıl olay şu...",
        f"Ben de eskiden zorlanıyordum ama şu basit taktiği keşfettim...",
        f"Uzmanlar bunu sizden saklıyor çünkü çok basit."
    ]
    
    cta = [
        "Daha fazlası için beni takip etmeyi unutma! 👇",
        "Part 2 için yorumlara 'DEVAM' yaz! 🔥",
        "Bunu arkadaşına gönder, o da öğrensin. ✈️"
    ]
    
    return {
        "hook": random.choice(hooks),
        "body": random.choice(body) + " (Buraya ürün/bilgi detayı gelecek)",
        "cta": random.choice(cta)
    }

# --- SONUÇ EKRANI ---
if st.button("🔥 VİRAL SENARYOMU YAZ"):
    if topic:
        with st.spinner('Yapay zeka viral veri tabanını tarıyor...'):
            script = generate_script(topic, tone)
            
            st.success("Senaryon Hazır!")
            
            st.markdown("### 🎣 Kanca (İlk 3 Saniye - Çok Önemli!)")
            st.info(script["hook"])
            
            st.markdown("### 📝 İçerik (Gövde)")
            st.write(script["body"])
            
            st.markdown("### 📣 Kapanış (Call to Action)")
            st.warning(script["cta"])
            
            st.caption("💡 İpucu: Kancayı söylerken ekrana yazı olarak da yaz!")
    else:
        st.error("Lütfen önce bir konu yaz!")