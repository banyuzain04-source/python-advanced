class Hero:
    def __init__(self, name, job, hp, race, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.max_hp = hp
        self.race = race
        self.type = hero_type  # "hero" / "normal" / "boss"
        print(f"✨ {self.name} memasuki arena! [HP: {self.hp}]")

    def is_alive(self):
        """Cek apakah karakter masih hidup"""
        # TODO: kembalikan True jika HP > 0, False jika tidak
        return self.hp > 0

    def display_status(self):
        """Tampilkan status karakter"""
        status = "🟢 Hidup" if self.is_alive() else "💀 Mati"
        print(f"[{self.name}] | Job: {self.job} | HP: {self.hp}/{self.max_hp} | STATUS: {status}")

    def attack(self, enemy, damage):
        """Melakukan serangan ke musuh"""
        # TODO:
        # 1. Cek apakah self masih hidup (pakai is_alive())
        if not self.is_alive():
            print(f"{self.name} tidak bisa menyerang karena sudah mati!")
            return

        # 2. Cek apakah damage valid (tidak boleh 0 atau negatif)
        if damage <= 0:
            print("Damage harus lebih dari 0!")
            return

        # 3. Hitung actual_damage (jika yang menyerang boss dan sudah <=50% HP, ia bisa kritikal)
        actual_damage = damage
        if self.type == "boss" and self.hp <= (0.5 * self.max_hp):
            actual_damage = int(damage * 1.5)
            print(f"⚡ {self.name} melakukan CRITICAL HIT ke {enemy.name}!")
        else:
            print(f"🗡️ {self.name} menyerang {enemy.name} dengan damage {damage}!")

        # 4. Panggil enemy.take_damage(actual_damage)
        enemy.take_damage(actual_damage)

    def take_damage(self, damage):
        """Menerima damage dan kurangi HP"""
        # TODO:
        # 1. Kurangi self.hp dengan damage
        self.hp -= damage
        # 2. Jika self.hp < 0, set menjadi 0
        if self.hp < 0:
            self.hp = 0
        # Jika ini boss dan baru saja turun ke <= 50% max HP, beri tanda Rage Mode
        if self.type == "boss":
            if self.hp <= (0.5 * self.max_hp) and not getattr(self, "rage_mode", False):
                self.rage_mode = True
                print(f"😈 {self.name} memasuki RAGE MODE!")

        # 3. Jika self.hp == 0, tampilkan "Karakter tewas"
        if self.hp == 0:
            print(f"{self.name} telah tewas!")
        # 4. Jika masih hidup, tampilkan sisa HP
        else:
            print(f"{self.name} menerima {damage} damage! Sisa HP: {self.hp}/{self.max_hp}")

    def heal(self):
        """Melakukan penyembuhan diri sendiri"""
        # TODO:
        # 1. Cek apakah self masih hidup, jika tidak, print pesan error
        if not self.is_alive():
            print(f"{self.name} tidak bisa menyembuhkan karena sudah mati!")
            return
        # 2. Tentukan heal_amount sesuai job:
        #    - Majo: 40
        #    - Tankā: 25
        #    - Job lain: 20
        # 3. Tambah self.hp dengan heal_amount
        # 4. Jika melebihi max_hp, set jadi max_hp
        # 5. Tampilkan pesan heal
        if self.job == "Majo":
            heal_amount = 30
        elif self.job == "Tankā":
            heal_amount = 25
        elif self.job == "Yuusha":
            heal_amount = 15   
        elif self.job == "Bokushi":
            heal_amount = 50

        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        pass


# ============ MEMBUAT KARAKTER ============
print("=" * 50)
print("🎮 SIMULASI RPG PARTY VS BOSS")
print("=" * 50 + "\n")

# PARTY HERO (3+ karakter)
yuusha = Hero("Himmel", "Yuusha", 120, "Human", "hero")
majo = Hero("Frieren", "Majo", 80, "Elf", "hero")
bokushi = Hero("Haiter", "Bokushi", 100, "Human", "hero")
tanka = Hero("Eisen", "Tankā", 150, "Dwarf", "hero")

# MUSUH
goblin = Hero("Goblin", "Monster", 60, "Goblin", "normal")
boss = Hero("Raja Iblis", "Boss", 200, "Akuma", "boss")

party = [yuusha, majo, bokushi, tanka]

print("\n" + "=" * 50)
print("⚔️ PERTEMPURAN DIMULAI!")
print("=" * 50 + "\n")

# ============ SIMULASI CERITA: DUNGEON LEVEL "SS" ============

print("\n📍 Dungeon Level: SS — Para pahlawan memasuki ruang bawah tanah...")
print("Para pahlawan melangkah perlahan, hati-hati namun tekad membara.\n")

# --- MUSUH PERTAMA: NAGA MERAH ---
red_dragon = Hero("Naga Merah", "Dragon", 180, "Dragon", "normal")
print("\n⚔️ PERTARUNGAN: Party vs Naga Merah")
print("-" * 40)

yuusha.attack(red_dragon, 40)   # Yuusha menyerang
red_dragon.attack(yuusha, 30)   # Naga membalas

majo.attack(red_dragon, 50)
red_dragon.attack(majo, 35)

bokushi.attack(red_dragon, 100)  # Serangan pamungkas

print(f"\n🎉 {red_dragon.name} telah dikalahkan! Namun para pahlawan luka-luka.")
print("Status sementara:")
for m in party:
    m.display_status()

# Sedikit istirahat: Bokushi mencoba menyembuhkan kelompok
print("\n✨ Bokushi berusaha menyembuhkan rekan-rekannya...")
bokushi.heal()
majo.heal()
print()

# --- MUSUH UTAMA: RAJA IBLIS ---
print("=" * 50)
print("📍 PERTARUNGAN BESAR: Party vs Raja Iblis (BOSS)")
print("-" * 50)

# buat boss baru dengan HP besar
boss = Hero("Raja Iblis", "Boss", 300, "Akuma", "boss")

# Serangan awal party
yuusha.attack(boss, 90)
majo.attack(boss, 60)  # Setelah ini boss turun ke 150 HP => memasuki Rage Mode
print()

# Balasan boss: Rage Mode aktif, serangan mematikan
if boss.is_alive():
    boss.attack(yuusha, 120)  # CRITICAL => Himmel tewas
    print()

if boss.is_alive():
    boss.attack(tanka, 80)   # Eisen terluka parah (sekarat)
    print()

# Serangan balasan dari sisa party
if majo.is_alive():
    bokushi.attack(boss, 90)
    majo.attack(boss, 70)

print()
if boss.is_alive():
    print(f"⚠️ {boss.name} masih hidup dengan {boss.hp} HP!")
else:
    print(f"\n🎊 {boss.name} telah dikalahkan! Namun kemenangan ini berharga mahal...")

# Akhir cerita — sedih tapi menang
print("\n--- EPILOG ---")
print("Para pahlawan keluar dari dungeon level SS dengan kemenangan, namun tidak tanpa kehilangan.")
print("Himmel gugur di medan laga, dan Eisen selamat namun nyaris tewas. Mereka membawa bekas luka dan kenangan.")

print("\n📊 STATUS AKHIR PARTY")
print("=" * 50)
for member in party:
    member.display_status()