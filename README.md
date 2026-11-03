import os
import sys
import pygame as pg

# 必須条件：カレントディレクトリをこのファイルがある場所に変更
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------
# 各自の追加機能を別ファイルからインポートする（仮のファイル名）
# 開発時は、各メンバーが自分のファイル（例: feature1.py）を作成して作業する
# ---------------------------------------------------------
# import feature1_player    # メンバー1（主人公移動・状態管理など）
# import feature2_effect    # メンバー2（丸焼きエフェクトなど）
# import feature3_timer     # メンバー3（キッチンタイマー機能など）
# import feature4_item      # メンバー4（アイテムや調理器具など）
# import feature5_enemy     # メンバー5（妨害キャラやスコア管理など）

class BasePlayer(pg.sprite.Sprite):
    """
    基本機能としての仮キャラクター。
    ※最終的にはメンバー1が拡張したクラスに差し替える想定。
    """
    def __init__(self):
        super().__init__()
        # 仮の赤い四角形を豪華豚とする
        self.image = pg.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:    self.rect.y -= 5
        if keys[pg.K_DOWN]:  self.rect.y += 5
        if keys[pg.K_LEFT]:  self.rect.x -= 5
        if keys[pg.K_RIGHT]: self.rect.x += 5

def main():
    pg.init()
    # 画面サイズやタイトルはチームで合意して変更すること
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("丸焼き豪華豚 - 共同開発ベース")
    clock = pg.time.Clock()

    # スプライトグループ（一括で更新・描画するための入れ物）
    all_sprites = pg.sprite.Group()

    # キャラクターのインスタンス化
    player = BasePlayer()
    all_sprites.add(player)

    # ---------------------------------------------------------
    # 各メンバーの機能のインスタンス化（例）
    # timer = feature3_timer.KitchenTimer()
    # ---------------------------------------------------------

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # キーボード入力など、イベント駆動の処理は各インスタンスに渡す
            # if event.type == pg.KEYDOWN:
            #     feature4_item.handle_event(event)

        # --- 更新処理 (Update) ---
        all_sprites.update()
        
        # 個別機能の更新処理をここで呼び出す
        # timer.update()
        # effect.update(player.rect)  # プレイヤーの座標を渡すなど

        # --- 描画処理 (Draw) ---
        screen.fill((255, 255, 255)) # 背景（白）
        
        # スプライトを一括描画
        all_sprites.draw(screen)

        # 個別機能の描画処理をここで呼び出す
        # timer.draw(screen)
        # effect.draw(screen)

        pg.display.update()
        clock.tick(60) # 60FPS

if __name__ == "__main__":
    main()