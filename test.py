import torch
from baseline.models.backbone.cswin import CSWin

def test_cswin():
    # 输入张量参数
    batch_size = 1
    channels = 64   # 根据 CSWin 类的 in_chans 参数
    height = 144    # 根据 CSWin 类的 img_size 参数
    width = 144     # 根据 CSWin 类的 img_size 参数

    # 创建输入张量
    input_tensor = torch.randn(batch_size, channels, height, width)

    # 实例化 CSWin 模型
    model = CSWin(img_size=144, patch_size=4, in_chans=64, embed_dim=512, depth=[1, 2, 21, 1], split_size=[7, 7, 7, 7],num_heads=[4, 8, 16, 32])

    # 将模型设置为评估模式
    model.eval()

    # 使用模型进行前向传播
    with torch.no_grad():
        outputs = model(input_tensor)

    # 输出每个张量的形状
    for i, output in enumerate(outputs):
        print(f"Output shape {i}: {output.shape}")

# 运行测试函数
test_cswin()
