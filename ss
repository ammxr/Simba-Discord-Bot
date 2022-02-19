@bot.command(aliases=["tst"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    compiled = Image.open ("background.png")
    headoverlay = Image.open ("testoverlay.png")
    asset= member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((349,349))
    compiled.paste(pfp, (72,122))
    compiled.paste(headoverlay, mask=headoverlay)
    compiled.save("profile.png")
    await ctx.send(file =discord.File("profile.png"))




@bot.command(aliases=["tz"])
async def uszerinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    img=cv2.imread("simmyleave.png")
    rows,cols,ch=img.shape

    pt1=np.float32([[0,0],[800,0],[0,600],[800,600]])
    pt2=np.float32([[56,65],[146,65],[56,165],[56,165]])

    matrix=cv2.getPerspectiveTransform(pt1,pt2)
    new_img=cv2.warpPerspective(img,matrix,(cols,rows))
    await ctx.send(file =discord.File(new_img))