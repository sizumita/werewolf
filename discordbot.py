# TODO
# オブジェクト
#   GM：bot
#   村
#   参加者
#       編成テンプレートの定義
#           4:村村占狼
#           5:村村村占狼
#   村人陣営の役職
#       村人
#       占い師
#   人狼陣営の役職
#       人狼
#   日数
#
# ゲーム進行
#   参加者の募集
#   プレイヤー参加
#   ゲーム開始
#   役職の割り振り
#   投票セット
#   占いセット
#   襲撃セット
#   処刑処理
#   襲撃処理
#   ゲーム終了判定
#   ゲーム結果の表示
#   日付変更処理
#   占い判定処理
#   襲撃結果(生存状況)表示
#       「Aさんが無残な姿で発見されました」
#   占い結果表示

from discord.ext import commands
import os
import traceback
from cogs.utils.errors import NoGuildError, PermissionNotFound

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_WEREWOLF_TOKEN']
bot.game_status = 'nothing'

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, NoGuildError):
        await ctx.send('サーバー内でのみ実行できるコマンドです')
        return

    if isinstance(error, PermissionNotFound):
        await ctx.send('コマンドを実行する権限がありません')
        return

    if isinstance(error, commands.CommandNotFound):
        # 要らなければ消してください
        return

    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


bot.load_extension('cogs.status')
bot.run(token)
