import discord
from discord.ext import commands
# Initialize bot with command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
# Waste classification data
WASTE_DATA = {
    'plastic bottle': {'category': 'Recyclable', 'action': 'Recycle', 'tips': 'Rinse before recycling. Consider reusing for storage.'},
    'apple core': {'category': 'Compostable', 'action': 'Compost', 'tips': 'Great for composting! Breaks down in 2-3 months.'},
    'battery': {'category': 'Hazardous waste', 'action': 'Special disposal', 'tips': 'Take to e-waste facility. Never throw in trash.'},
    'paper': {'category': 'Recyclable', 'action': 'Recycle', 'tips': 'Separate from wet waste. Reuse for notes first.'},
    'food scraps': {'category': 'Compostable', 'action': 'Compost', 'tips': 'Composting creates nutrient-rich soil in 3-6 months.'},
    'aluminum can': {'category': 'Recyclable', 'action': 'Recycle', 'tips': 'Aluminum is infinitely recyclable. Rinse first.'},
    'plastic bag': {'category': 'Trash', 'action': 'Trash', 'tips': 'Bring reusable bags next time. Most facilities cannot recycle bags.'},
    'glass': {'category': 'Recyclable', 'action': 'Recycle', 'tips': 'Separate by color if required. Reuse jars for storage.'},
    'light bulb': {'category': 'Hazardous waste', 'action': 'Special disposal', 'tips': 'Contains mercury. Never throw in regular trash.'},
    'cardboard': {'category': 'Recyclable', 'action': 'Recycle', 'tips': 'Flatten boxes to save space. Reuse for storage or shipping.'},
}
COMPOSTING_INFO = "Composting breaks down organic matter into nutrient-rich soil. Suitable items: fruit/vegetable scraps, coffee grounds, leaves, grass clippings, paper, cardboard. Avoid: meat, dairy, oils."
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
@bot.command(name='eco')
async def classify_waste(ctx, *, item: str):
    """Classify waste and provide environmental advice."""
    item_lower = item.lower().strip()
    
    # Search for item in database
    waste_info = None
    for key in WASTE_DATA:
        if key in item_lower or item_lower in key:
            waste_info = WASTE_DATA[key]
            break
    
    if not waste_info:
        await ctx.send(f"❓ I'm not sure about '{item}'. Try common items like: plastic bottle, apple core, battery, paper, food scraps, aluminum can, glass, cardboard.")
        return
    
    # Build response
    embed = discord.Embed(title=f"♻️ Waste Classification: {item.title()}", color=discord.Color.green())
    embed.add_field(name="Category", value=waste_info['category'], inline=False)
    embed.add_field(name="Recommended Action", value=waste_info['action'], inline=False)
    embed.add_field(name="💡 Environmental Tips", value=waste_info['tips'], inline=False)
    
    if waste_info['category'] == 'Compostable':
        embed.add_field(name="🌱 Composting Info", value=COMPOSTING_INFO, inline=False)
    
    await ctx.send(embed=embed)
@bot.command(name='help_eco')
async def eco_help(ctx):
    """Display help for eco commands."""
    embed = discord.Embed(title="♻️ Eco-Friendly Assistant Help", color=discord.Color.green())
    embed.add_field(name="!eco <item>", value="Classify waste and get environmental advice.", inline=False)
    embed.add_field(name="Example", value="!eco plastic bottle", inline=False)
    embed.add_field(name="Categories", value="Recyclable, Compostable, Hazardous waste, Trash", inline=False)
    await ctx.send(embed=embed)
# Replace with your bot token
bot.run("TOKEN")
