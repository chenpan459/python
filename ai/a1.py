# 导入必要的库
from modelscope.pipelines import pipeline
import cv2
import datasets

# 尝试导入 OfflineModeIsEnabled，如果失败则使用 is_offline_mode
try:
    from datasets.utils.file_utils import OfflineModeIsEnabled
except ImportError:
    from datasets.utils.logging import is_offline_mode as OfflineModeIsEnabled

# 检查离线模式
if OfflineModeIsEnabled():
    print("Offline mode is enabled")
else:
    print("Offline mode is not enabled")

# 初始化管道
cartoon_pipeline = pipeline('image_portrait_stylization', model='OwenWang/Portrait-Cartoonization')

# 读取输入图像
input_image_path = 'D:\\ai\\2c.jpg'
output_image_path = 'D:\\ai\\2c_cartoon.jpg'

input_image = cv2.imread(input_image_path)

# 调用模型进行卡通化处理
result = cartoon_pipeline(input_image)

# 保存结果图像
cv2.imwrite(output_image_path, result['output_img'])

print(f"Cartoonized image saved to {output_image_path}")