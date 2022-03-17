import argparse
import asyncio
import os
import aiohttp
import aiofiles
import sys

URL = "https://picsum.photos/700"


async def helper(filename, session):
    async with session.get(URL) as response:
        if response.status == 200:
            async with aiofiles.open(filename, mode='bw') as file:
                await file.write(await response.read())


async def load_images(images_number: int, path: str):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(helper(f"{path}/image_{i + 1}.png", session) for i in range(images_number)))


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Advanced python hw05')
    parser.add_argument('--images_number', help='Total number of images', type=int)
    parser.add_argument('--dir_path', help='Path to directory with images', type=str)
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args(sys.argv[1:])
    if not os.path.exists(args.dir_path):
        os.makedirs(args.dir_path)
    asyncio.run(load_images(args.images_number, args.dir_path))
