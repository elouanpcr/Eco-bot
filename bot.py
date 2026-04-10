import discord
from discord import app_commands

# ---------- CONFIG ----------
TOKEN = "TU_TOKEN_AQUI"
CANAL_ID = 123456789012345678  # ID del canal de bienvenida

# ---------- CLIENT ----------
class EcoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash commands sincronizados")

bot = EcoBot()

# ---------- DATA ----------
WASTE_DATA = {
    "vidrio": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Sepáralo por color si es necesario y un enjuague."
    },
    "botella plastica": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Enjuágala antes de reciclarla."
    },
    "papel": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Mantenlo seco y limpio."
    },
    "carton": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Aplana las cajas antes de reciclar."
    },
    "latas": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Enjuaga las latas antes de reciclar y aplanalas."
    },
    "bateria": {
        "category": "Peligroso",
        "action": "Desecho especial",
        "tips": "Llévala a un punto limpio o reciclaje electrónico."
    },
    "residuos electronicos": {
        "category": "Peligroso",
        "action": "Residuos electrónicos",
        "tips": "No los botes a la basura común."
    }
}


# ---------- EVENTO INICIO ----------
@bot.event
async def on_ready():
    print(f"✅ Conectado como {bot.user}")

    canal = bot.get_channel(CANAL_ID)
    if canal:
        embed = discord.Embed(
            title="🌱 EcoBot listo",
            description="Usa /eco para clasificar residuos ♻️",
            color=discord.Color.green()
        )
        await canal.send(embed=embed)

# ---------- COMANDO ECO ----------
@bot.tree.command(name="eco", description="Clasifica residuos y entrega consejos ecológicos")
@app_commands.describe(item="Ej: glass, paper, battery...")
async def eco(interaction: discord.Interaction, item: str):
    item = item.lower()

    if item not in WASTE_DATA:
        await interaction.response.send_message(
            f"❌ No conozco **{item}**\n💡 Usa: glass, paper, battery, plastic bottle...",
            ephemeral=True
        )
        return

    data = WASTE_DATA[item]

    embed = discord.Embed(
        title=f"♻️ {item.title()}",
        color=discord.Color.green()
    )
    embed.add_field(name="Categoría", value=data["category"], inline=False)
    embed.add_field(name="Acción", value=data["action"], inline=False)
    embed.add_field(name="Consejo", value=data["tips"], inline=False)
    embed.set_footer(text="EcoBot 🌱 - Cuida el planeta")

    await interaction.response.send_message(embed=embed)

# ---------- COMANDO AYUDA ----------
@bot.tree.command(name="ayuda", description="Ver cómo usar EcoBot")
async def ayuda(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌱 EcoBot - Ayuda",
        description="Bot para clasificar residuos fácilmente ♻️",
        color=discord.Color.green()
    )

    embed.add_field(
        name="Comandos",
    value=(
    "/eco vidrio\n"
    "/eco botella plastica\n"
    "/eco papel\n"
    "/eco carton\n"
    "/eco latas\n"
    "/eco bateria\n"
    "/eco residuos electronicos"
    ),
    inline=False
    )

    embed.add_field(
        name="Ejemplo",
        value="/eco vidrio",
        inline=False
    )

    embed.set_footer(text="EcoBot 🌱")

    await interaction.response.send_message(embed=embed)

# ---------- RUN ----------
bot.run("TOKEN")
