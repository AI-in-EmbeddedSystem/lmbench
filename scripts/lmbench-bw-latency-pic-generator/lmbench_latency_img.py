import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_latency_vs_size(folder_path, output_image_path='latency_vs_size.png'):
    # 设置图片尺寸，这里宽度为 10 英寸，高度为 6 英寸
    plt.figure(figsize=(15, 6))


    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    # 读取 CSV 文件
                    df = pd.read_csv(file_path)
                    # 将 size(byte) 列数据乘以 1000
                    df['size(byte)'] = df['size(byte)'] * 1000
                    size = df['size(byte)']
                    latency = df['latency(ns)']

                    # 绘制线条图，使用文件名作为图例
                    plt.plot(size, latency, label=file)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")

    # 设置图表标题和坐标轴标签
    plt.title('lat_mem_rd')
    plt.xlabel('Size (byte)')
    plt.ylabel('Latency (ns)')

    plt.xscale('log', base=2)
    plt.yscale('log',base=2)

    # 设置x轴刻度为：1K, 2K, 4K, 8K,16K,32K,64K,128K,256K,512K,1M,2M,4M,8M,16M,32M,64M,128M,256M, 512M, 1G
    x_ticks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
    x_tick_labels = ['1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', '1M', '2M', '4M', '8M', '16M', '32M', '64M', '128M', '256M', '512M', '1G']

    plt.xticks(x_ticks, x_tick_labels)

    plt.yticks([1, 2, 4, 8, 16, 32, 64, 128, 256], [1, 2, 4, 8, 16, 32, 64, 128, 256])

    # 显示图例
    plt.legend(loc='upper left')

    # 保存图片
    plt.savefig(output_image_path)

    # 关闭图表
    plt.close()

    print(f"图片已保存至 {output_image_path}")


# 使用示例
if __name__ == "__main__":
    folder_path = r'latency_data'  # 替换为实际的 CSV 文件路径
    plot_latency_vs_size(folder_path)

