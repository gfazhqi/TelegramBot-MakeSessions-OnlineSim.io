from telethon.sync import Button

class AllButtons:
    admin_buttons = [
        [Button.inline('💲 Panel Balance 💲', b'balance')],
        [Button.inline('🔮 Create Session 🔮', b'create')]
    ]
    
    country_name_buttons = [
        [Button.inline("🇻🇳 Vietnam 🇻🇳", b"84"), Button.inline("🇮🇳 India 🇮🇳", b"91"), Button.inline("🇮🇩 Indonesia 🇮🇩", b"62")],
        [Button.inline("🇧🇷 Brazil 🇧🇷", b"55"), Button.inline("🇰🇿 Kazakhstan 🇰🇿", b"77"), Button.inline("🇮🇱 Israel 🇮🇱", b"972")],
        [Button.inline("🇮🇪 Ireland 🇮🇪", b"353"), Button.inline("🇦🇫 Afghanistan 🇦🇫", b"93"), Button.inline("🇪🇬 Egypt 🇪🇬", b"20")],
        [Button.inline("🇦🇷 Argentina 🇦🇷", b"54"), Button.inline("🇲🇽 Mexico 🇲🇽", b"52"), Button.inline("🇻🇪 Venezuela 🇻🇪", b"58")],
        [Button.inline("🇳🇵 Nepal 🇳🇵", b"977"), Button.inline("🇧🇾 Belarus 🇧🇾", b'375'), Button.inline("🇹🇭 Thailand 🇹🇭", b"66")]
    ]
