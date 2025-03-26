# SleepyKoala - Thumby用ゲーム
# コアラを左右に動かして上から降る火を避けるゲーム
from thumbyGraphics import display
from thumbySprite import Sprite
import thumbyButton as buttons
import random
Number = int
from thumbyAudio import audio
from thumbySaves import saveData

# グローバル変数の定義
fire_1_x = None
fire_1_y = None
fire_2_x = None
fire_2_y = None
koala = None
Main_menu = None
score = None
fire_1 = None
fire_2 = None
odd_or_even = None
koala_x = None

# 初期スプライトの仮定義
Main_menu = Sprite(1, 1, bytearray([1]))
fire_2 = Sprite(1, 1, bytearray([1]))
fire_1 = Sprite(1, 1, bytearray([1]))
koala = Sprite(1, 1, bytearray([1]))

# ゲームのメイン処理
def Game():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    koala.setFrame(0)  # コアラの初期フレームを設定
    odd_or_even = 0    # 未使用の変数（元のコードから保持）
    score = 0          # スコアの初期化
    koala_x = 28       # コアラの初期X位置
    fire_1_x = 12      # 火1の初期X位置
    fire_2_x = 12      # 火2の初期X位置
    koala.x = koala_x  # コアラのスプライト位置を設定
    koala.y = 22       # コアラのY位置（固定）
    spawn_fire_1()     # 火1の生成
    spawn_fire_2()     # 火2の生成
    # メインメニュー表示ループ
    while not buttons.buttonA.justPressed():
        display.setFont("/lib/font3x5.bin", 3, 5, display.textSpaceWidth)
        display.drawSprite(Main_menu)
        display.drawText(str('Press'), 48, 25, 1)
        display.drawText(str('-A-'), 55, 32, 1)
        display.update()
        display.fill(0)
    # ゲームループ開始
    while True:
        main_game_loop()

# 火1の生成
def spawn_fire_1():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_1_x = random.choice([28, 44, 12])  # ランダムなX位置
    fire_1_y = -48                         # 画面外の上から開始
    fire_1.x = fire_1_x
    fire_1.y = fire_1_y

# メインゲームループ
def main_game_loop():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    # 火1が画面外に出たらスコア加算と再生成
    if fire_1_y > 50:
        score = (score if isinstance(score, Number) else 0) + 1
        respawn_fire_1()
    # 火2が画面外に出たらスコア加算と再生成
    if fire_2_y > 30:
        score = (score if isinstance(score, Number) else 0) + 1
        respawn_fire_2()
    # 左移動
    if buttons.buttonL.justPressed() and koala_x > 12:
        audio.play(1000, 50)
        for count in range(16):
            score2()
            draw_fire_1()
            draw_fire_2()
            koala.setFrame(2)  # 左移動時のアニメーション
            display.drawSprite(koala)
            display.update()
            if fire_1_y > 8:
                fire_1_collision_check()
            if fire_2_y > 8:
                fire_2_collision_check()
            display.fill(0)
            koala_x = (koala_x if isinstance(koala_x, Number) else 0) - 1
            koala.x = koala_x
        koala.setFrame(0)  # 静止フレームに戻す
    # 右移動
    if buttons.buttonR.justPressed() and koala_x < 44:
        audio.play(1000, 50)
        for count2 in range(16):
            score2()
            draw_fire_1()
            draw_fire_2()
            koala.setFrame(1)  # 右移動時のアニメーション
            display.drawSprite(koala)
            display.update()
            if fire_1_y > 8:
                fire_1_collision_check()
            if fire_2_y > 8:
                fire_2_collision_check()
            display.fill(0)
            koala_x = (koala_x if isinstance(koala_x, Number) else 0) + 1
            koala.x = koala_x
        koala.setFrame(0)  # 静止フレームに戻す
    # 描画と更新
    draw_fire_1()
    draw_fire_2()
    display.drawSprite(koala)
    score2()
    display.update()
    if fire_1_y > 8:
        fire_1_collision_check()
    if fire_2_y > 8:
        fire_2_collision_check()
    display.fill(0)

# 火2の生成
def spawn_fire_2():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_2_x = random.choice([28, 44, 12])
    fire_2_y = -80
    fire_2.x = fire_2_x
    fire_2.y = fire_2_y

# 火1の再生成
def respawn_fire_1():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_1_x = random.choice([44, 28, 12])
    fire_1_y = -48
    fire_1.x = fire_1_x
    fire_1.y = fire_1_y

# 火2の再生成
def respawn_fire_2():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_2_x = random.choice([44, 28, 12])
    fire_2_y = -80
    fire_2.x = fire_2_x
    fire_2.y = fire_2_y

# 火2の描画と移動
def draw_fire_2():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_2_y = (fire_2_y if isinstance(fire_2_y, Number) else 0) + 1
    fire_2.y = fire_2_y
    display.drawSprite(fire_2)

# 火1の描画と移動
def draw_fire_1():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    fire_1_y = (fire_1_y if isinstance(fire_1_y, Number) else 0) + 1
    fire_1.y = fire_1_y
    display.drawSprite(fire_1)

# スコア表示
def score2():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    display.drawText(str(score), 0, 0, 1)

# 火1との衝突判定
def fire_1_collision_check():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    if bool(display.getPixel(fire_1_x + 2, fire_1_y + 2)) == True or bool(display.getPixel(fire_1_x + 2, fire_1_y + 2)) == True:
        Game_over()
    if bool(display.getPixel(fire_1_x + 2, fire_1_y + 2)) == True or bool(display.getPixel(fire_1_x + 2, fire_1_y + 2)) == True:
        Game_over()

# 火2との衝突判定
def fire_2_collision_check():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    if bool(display.getPixel(fire_2_x + 2, fire_2_y + 2)) == True or bool(display.getPixel(fire_2_x + 2, fire_2_y + 2)) == True:
        Game_over()
    if bool(display.getPixel(fire_2_x + 2, fire_2_y + 2)) == True or bool(display.getPixel(fire_2_x + 2, fire_2_y + 2)) == True:
        Game_over()

# ハイスコア保存の設定
saveData.setName(globals().get('__file__', 'FAST_EXECUTE').replace('/Games/', '').strip('/').split('/')[0].split('.')[0])

# ゲームオーバー処理
def Game_over():
    global fire_1_x, fire_1_y, fire_2_x, fire_2_y, koala, Main_menu, score, fire_1, fire_2, odd_or_even, koala_x
    audio.play(800, 1000)  # ゲームオーバー音
    if saveData.getItem('high score') == None:
        saveData.setItem('high score', 0)
        saveData.save()
    if saveData.getItem('high score') < score:
        saveData.setItem('high score', score)
        saveData.save()
    # スコア表示ループ
    while not buttons.buttonA.justPressed():
        display.setFont("/lib/font8x8.bin", 8, 8, display.textSpaceWidth)
        display.fill(0)
        display.drawText(str(score), 32, 10, 1)
        display.drawText(str(saveData.getItem('high score')), 32, 30, 1)
        display.setFont("/lib/font5x7.bin", 5, 7, display.textSpaceWidth)
        display.drawText(str('score'), 20, 0, 1)
        display.drawText(str('high score'), 5, 20, 1)
        display.update()
        display.fill(0)
    Game()  # ゲーム再開

# ビットマップ定義
koala_map = bytearray([124, 196, 24, 88, 28, 220, 222, 30, 94, 30, 28, 236,
                       0, 3, 4, 8, 8, 13, 9, 10, 6, 9, 9, 6])  # 幅: 12, 高さ: 12
fire_map = bytearray([192, 152, 240, 230, 255, 253, 248, 240, 156, 192,
                      0, 1, 3, 3, 3, 3, 3, 3, 1, 0])  # 幅: 10, 高さ: 10

# FPS設定とスプライトの初期化
display.setFPS(30)
Main_menu = Sprite(52, 50, bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,192,192,192,224,224,224,240,240,240,240,248,248,248,248,248,248,248,240,240,224,96,192,128,0,0,0,0,0,0,0,0,0,252,6,2,2,2,6,4,136,240,224,240,208,248,248,252,254,255,255,255,255,255,255,255,255,255,255,255,255,247,255,255,239,239,255,255,191,159,31,31,159,255,254,249,254,252,252,248,0,0,0,0,0,127,128,0,0,0,0,0,129,131,131,195,3,3,3,3,3,3,1,1,129,129,129,128,128,128,0,0,0,0,0,0,1,129,129,131,3,1,0,0,0,1,131,195,65,33,48,24,7,0,0,0,0,0,1,2,2,255,0,0,7,15,4,4,7,0,0,0,0,0,188,255,1,1,1,1,1,135,252,128,0,0,0,0,6,7,12,141,135,192,192,224,224,240,255,184,224,128,0,0,0,0,0,0,0,0,0,0,0,3,12,16,32,64,128,128,0,0,0,0,0,0,0,1,35,226,162,226,1,1,0,1,3,13,225,253,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,12,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,2,2,2,2,3,3,2,2,3,1,1,1,3,13,23,31,47,63,63,63,63,63,63,63,31,31,15,11,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), 0, 0, 0, 0, 0)
fire_1 = Sprite(10, 10, fire_map, 0, 0, 0, 0, 0)
fire_2 = Sprite(10, 10, fire_map, 0, 0, 0, 0, 0)
koala = Sprite(12, 12, koala_map, 0, 0, 0, 0, 0)
koala.key = 0
fire_1.key = 0
fire_2.key = 0

# ゲーム開始
Game()