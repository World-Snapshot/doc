from PIL import Image
import numpy as np
import os

def process_image(input_path, output_path, grid_size=3):
    """
    处理图像，保留每个grid_size x grid_size网格中的中心像素
    其他像素设为透明
    
    参数:
    input_path: 输入图像路径
    output_path: 输出图像路径
    grid_size: 网格大小，默认为3
    """
    # 读取图像
    img = Image.open(input_path)
    
    # 转换为RGBA模式以支持透明度
    img = img.convert('RGBA')
    
    # 转换为numpy数组
    img_array = np.array(img)
    
    # 获取图像尺寸
    height, width = img_array.shape[:2]
    
    # 创建一个全透明的输出图像
    output_array = np.zeros_like(img_array)
    output_array[:, :, 3] = 0  # 设置alpha通道为0（完全透明）
    
    # 计算中心像素的偏移
    center_offset = grid_size // 2
    
    # 遍历每个网格
    for y in range(center_offset, height - center_offset, grid_size):
        for x in range(center_offset, width - center_offset, grid_size):
            # 只保留中心像素
            output_array[y, x] = img_array[y, x]
    
    # 创建新图像
    output_img = Image.fromarray(output_array)
    
    # 保存结果
    output_img.save(output_path, 'PNG')
    
    print(f"处理完成！输出文件: {output_path}")
    
    # 返回处理后的图像用于显示
    return output_img

def main():
    # 设置输入输出路径
    input_path = 'tt4.png'  # 替换为你的输入图像路径
    output_path = 'output_grid.png'
    
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"错误：找不到输入文件 {input_path}")
        return
    
    try:
        # 处理图像
        processed_img = process_image(input_path, output_path)
        
        # 打印原始图像和处理后图像的尺寸
        with Image.open(input_path) as img:
            print(f"原始图像尺寸: {img.size}")
        print(f"处理后图像尺寸: {processed_img.size}")
        
    except Exception as e:
        print(f"处理图像时出错: {str(e)}")

if __name__ == "__main__":
    main()