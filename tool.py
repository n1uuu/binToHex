import sys
import argparse


def bin_to_hex_string(bin_file_path):
    try:
        # 读取二进制文件内容
        with open(bin_file_path, 'rb') as bin_file:
            bin_data = bin_file.read()


        hex_string = ', '.join(f'0x{byte:02x}' for byte in bin_data)

        # 返回格式化的Go语言切片格式字符串
        return f"[]byte{{{hex_string}}}"
    except Exception as e:
        return f"发生错误: {e}"


def main():
    parser = argparse.ArgumentParser(description='将二进制文件内容转换为十六进制格式')
    parser.add_argument('-f', '--file', required=True, help='指定要转换的二进制文件')
    parser.add_argument('-o', '--output', help='指定输出文件名，将结果保存到该文件')

    args = parser.parse_args()

    result = bin_to_hex_string(args.file)

    if args.output:
        try:
            with open(args.output, 'w') as output_file:
                output_file.write(result)
            print(f"转换结果已保存到 {args.output}")
        except Exception as e:
            print(f"无法写入输出文件: {e}")
    else:
        print(result)


if __name__ == '__main__':
    main()
