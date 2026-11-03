import os
import sys
import pygame as pg

# 必須条件：カレントディレクトリをこのファイルがある場所に変更
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------
# 【追加機能のインポート領域】
# 各メンバーは自分の担当機能が完成したら、コメントアウトを外して結合する
# ---------------------------------------------------------
# import feature_player    # 追加機能1：プレイヤーアクション拡張
# import feature_item      # 追加機能2：落下アイテム生成
# import feature_hazard    # 追加機能3：お邪魔ギミック生成
# import feature_system    # 追加機能4：タイマー・スコア管理
# import feature_ui        # 追加機能5：UI・エフェクト演出

class BasePlayer(pg.sprite.Sprite):
    """
    基本機能としてのミニマムなプレイヤー。
    ※単体で動くための仮実装。左右にしか動けない（キャッチゲーム用）。
    """
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((60, 20))
        self.image.fill((0, 0, 255)) # 仮の姿（青い横長の箱）
        # 画面下部に配置
        self.rect = self.image.get_rect(center=(400, 550))

    def update(self):
        keys = pg.key.get_pressed()
        # 左右移動のみ許可。画面外に出ないように制限。
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 6
        if keys[pg.K_RIGHT] and self.rect.right < 800:
            self.rect.x += 6

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("アイテムキャッチ・パニック - 拡張ベース")
    clock = pg.time.Clock()

    all_sprites = pg.sprite.Group()

    # プレイヤー（受け皿）のインスタンス化
    player = BasePlayer()
    all_sprites.add(player)

    # ---------------------------------------------------------
    # 【追加機能の初期化領域】
    # ---------------------------------------------------------
    # item_manager = feature_item.ItemManager()
    # hazard_manager = feature_hazard.HazardManager()
    # game_system = feature_system.GameSystem()
    # ui_manager = feature_ui.UIManager()

    while True:
        # --- イベント処理 ---
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # 各追加機能へのイベント伝達
            # game_system.handle_event(event)

        # --- 更新処理 (Update) ---
        all_sprites.update()
        
        # 追加機能の更新（プレイヤーの座標を渡して当たり判定を行わせる）
        # item_manager.update(player.rect)
        # hazard_manager.update(player.rect)
        # game_system.update()

        # --- 描画処理 (Draw) ---
        screen.fill((240, 255, 240)) # 背景（薄い緑色）
        
        # キャラクター（受け皿など）の一括描画
        all_sprites.draw(screen)

        # 落下物やUIなどを描画する追加機能
        # item_manager.draw(screen)
        # hazard_manager.draw(screen)
        # ui_manager.draw(screen)

        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()