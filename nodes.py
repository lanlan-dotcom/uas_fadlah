# nodes.py

from tree import Node

# =========================
# ENDING NODES
# =========================

dead_end = Node(
    title="DEAD END - BASMENT",
    text="""
Sesosok monster melangkah keluar dari kegelapan basement.
Tubuhnya yang menjulang tinggi terlilit rantai-rantai tua yang menyeret di lantai, meninggalkan suara gesekan yang mengerikan. Di balik wajahnya yang samar, sepasang mata merah menyala menembus kegelapan.
Jantungmu berdegup kencang. Namun semuanya sudah terlambat.
Monster itu menerjang dan menerkammu.

☠️ DEAD END
""",
    ending=True,

    sound="asset/sound/scream.mp3",
    image="asset/image/monster.png"
)

cursed_end = Node(
    title="CURSED END - LOTENG",
    text="""
Boneka itu perlahan menoleh ke arahmu.
Terdengar tawa pelan yang menggema di dalam ruangan yang sunyi.
Tubuhmu mulai membeku. Kamu mencoba bergerak, tetapi seluruh anggota tubuhmu seolah kehilangan kendali.
Pandanganmu perlahan mengabur, sementara senyum boneka itu semakin lebar.

👁️ CURSED END
""",
    ending=True,

    sound="asset/sound/boneka.mp3",
    image="asset/image/boneka.png"
)

survive_end = Node(
    title="SURVIVE END - LEMARI",
    text="""
Kamu bersembunyi di dalam lemari.
Udara sempit membuat napasmu tertahan.
Pintu kamar terbuka.
Sesuatu masuk tanpa tergesa, memeriksa ruangan dengan tenang.
Langkah itu mendekat ke lemari… berhenti… lalu perlahan menjauh.
Beberapa menit kemudian, semuanya kembali sunyi.
Kamar ini kosong lagi dan kamu tetap di sana sampai cahaya pagi datang.

✅ SURVIVE END
""",
    ending=True,

    sound="asset/sound/selamat.mp3",
    image="asset/image/lemari.png"
)

survive_end_2 = Node(
    title="SURVIVE END - DAPUR",
    text="""
Monster itu melewati meja dapur tanpa menyadari bahwa kamu bersembunyi di sana.
Setelah beberapa menit yang menegangkan, langkahnya semakin menjauh hingga akhirnya menghilang.
Kini hanya tersisa keheningan.

✅ SURVIVE END
""",
    ending=True,

    sound="asset/sound/selamat.mp3",
    image="asset/image/safe_dapur.png"
)

jumpscare_end = Node(
    title="DEAD END - KAMAR ASING",
    text="""
Kamu memilih untuk kembali tidur, mencoba mengabaikan semuanya.
Selimut terasa ditarik pelan… lalu semakin kuat, seolah ada sesuatu di bawah kasur.
Kamu memaksa diri menutup mata.
Sesaat kemudian—karena penasaran kamu melihat ke bawah kasur

BRRAAAK!!

Sosok itu menyembur keluar dari bawah kasur.
Sepasang mata merah langsung mengunci pandanganmu, lalu tanpa ragu ia menerkam.

😨 DEAD END
""",
    ending=True,

    sound="asset/sound/scream.mp3",
    image="asset/image/kolong.png"
)

safe_path = Node(
    title="SAFE PATH - LOTENG",
    text="""
Dengan senter di tangan, kamu menemukan sebuah lorong rahasia.
Lorong itu tampak gelap dan sempit, tetapi mungkin inilah jalan keluar yang selama ini kamu cari.

🔦 SAFE PATH
""",
    ending=True,

    sound="asset/sound/selamat.mp3",
    image="asset/image/keluar.png"
)

safe_path_2 = Node(
    title="SAFE PATH - DAPUR",
    text="""
Dengan Kunci Utama yang ditemukan di dapur, kamu membuka pintu rahasia yang tersembunyi di pojok ruangan.
Di baliknya terdapat jalan keluar.
Kamu berhasil melarikan diri dari rumah tersebut.

✅ SURVIVE END
""",
    ending=True,

    sound="asset/sound/selamat.mp3",
    image="asset/image/keluar_dapur.png"
)

# =========================
# LEVEL 2 NODES
# =========================

basement = Node(
    title="LANTAI DASAR",
    text="""
Kamu berdiri di depan pintu basement.
Dari balik pintu, terdengar suara rantai bergemerincing yang samar namun jelas memecah keheningan.
Udara terasa semakin dingin, dan firasat buruk mulai menghantuimu.

Apa yang akan kamu lakukan?
""",

    choice1="Buka Basement",
    choice2="Cari Dapur",

    sound="asset/sound/chain.mp3",
    image="asset/image/depan_dapur.png"
)

kitchen = Node(
    title="DAPUR",
    text="""
Kamu memasuki dapur tua yang remang-remang.
Noda darah yang telah mengering terlihat di lantai dan dinding, sementara aroma besi memenuhi udara.
Di atas meja kayu yang usang, terdapat dua benda yang mencolok:

🔪 Pisau

🗝️ Kunci Utama

Keduanya tampak penting, tetapi kamu hanya punya waktu untuk memilih satu.
Apa yang ingin kamu ambil?
""",

    choice1="Ambil Pisau",
    choice2="Ambil Kunci Utama",

    sound="asset/sound/rain.mp3",
    image="asset/image/dapur.png"
)

attic = Node(
    title="LOTENG",
    text="""
Loteng itu terasa jauh lebih dingin daripada ruangan lainnya.
Debu beterbangan di udara, sementara lantai kayu berderit pelan di bawah kakimu.
Di tengah kegelapan, cahaya samar memperlihatkan dua benda:

🧸 Boneka Tua
🔦 Senter

Kamu harus memilih dengan hati-hati.
Apa yang ingin kamu ambil?
""",

    choice1="Ambil Boneka",
    choice2="Ambil Senter",

    sound="asset/sound/loteng.mp3",
    image="asset/image/loteng.png"
)

stay_room = Node(
    title="KAMAR ASING",
    text="""
Kamu tetap di dalam kamar.
Dari kejauhan, terdengar langkah kaki di lorong rumah. Pelan, teratur, seperti sedang berjalan tanpa terburu-buru.
Semakin lama, suara itu makin dekat ke arah kamar ini.
Untuk sesaat, kamu mencoba meyakinkan diri bahwa ini hanya mimpi. Mungkin kamu akan terbangun nanti, dan semuanya akan hilang.
Tapi rasa takutnya terlalu nyata untuk diabaikan.

Apa yang akan kamu lakukan?
""",

    choice1="Sembunyi di Lemari",
    choice2="Tidur Lagi",

    sound="asset/sound/jejak_kaki.mp3",
    image="asset/image/hujan.png"
)

hallway = Node(
    title="LORONG",
    text="""
Kamu membuka pintu kamar dan melangkah keluar.
Lorong rumah tampak sepi, hanya diterangi lampu yang berkedip-kedip di langit-langit.
Bayangan aneh menari di sepanjang dinding, sementara suara lantai kayu berderit pelan di bawah kakimu.

Ke mana kamu akan pergi?

""",

    choice1="Turun Tangga",
    choice2="Masuk Loteng",

    sound="asset/sound/lampu.mp3",
    image="asset/image/lorong.png"
)

# =========================
# ROOT NODE
# =========================

start = Node(
    title="AWAL PETUALANGAN - KAMAR ASING",
    text="""
Kamu terbangun di kamar yang tidak kamu kenali.
Hujan terdengar dari luar, tapi terlalu jauh untuk dipastikan.  
Lampu mati. Pintu kamar sedikit terbuka.
Kamu mencoba berpikir ini hanya mimpi.
Tapi tubuhmu tidak setuju.
Rumah ini terlalu sunyi untuk sesuatu yang tidak nyata.

Apa yang akan kamu lakukan?""",

    choice1="Keluar Kamar",
    choice2="Tetap di Kamar",

    sound="asset/sound/rain.mp3",
    image="asset/image/hujan.png"
)

# =========================
# CONNECT TREE
# =========================

# Root connections
start.next1 = hallway
start.next2 = stay_room

# Hallway connections
hallway.next1 = basement
hallway.next2 = attic

# Basement connections
basement.next1 = dead_end
basement.next2 = kitchen

# Kitchen connections
kitchen.next1 = survive_end_2
kitchen.next2 = safe_path_2

# Attic connections
attic.next1 = cursed_end
attic.next2 = safe_path

# Stay room connections
stay_room.next1 = survive_end
stay_room.next2 = jumpscare_end