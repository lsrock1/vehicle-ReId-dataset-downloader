import os

# ref https://medium.com/@acpanjan/download-google-drive-files-using-wget-3c2c025a8b99
share_urls = [
    'https://drive.google.com/file/d/1p8kjYVI1Bkj2LcC2y2Kv5lD0FalzgkpR/view?usp=sharing', # 1
    'https://drive.google.com/file/d/1lAwOdb5qVytL239YzbvxMcEihkjAM92m/view?usp=sharing', # 2
    'https://drive.google.com/file/d/19NnMttzJ1x6n8i48tm6R_LM_wXgo9AnL/view?usp=sharing', # 3
    'https://drive.google.com/file/d/155_m-3MUYuXKJ9F4bV5Av4bN_JG8P-6s/view?usp=sharing', # 4
    'https://drive.google.com/file/d/1G5yikBZxSeoDE7CMECe0zjJq4dy8YNlQ/view?usp=sharing', # 5
    'https://drive.google.com/file/d/1tlGa71UkAklRCroLX9WSGQiIOqYoxqC9/view?usp=sharing', # 6
    'https://drive.google.com/file/d/1zjmoIEiYJqa1ERWRs_M1to4sqr9DCKpI/view?usp=sharing', # 7
    'https://drive.google.com/file/d/1pmi6PTs5fZLxfp-pgkh0SobrjWPpXBPx/view?usp=sharing', # 8
    'https://drive.google.com/file/d/1hZ8Lh4ZiDsfEAdMlpZ6MTsrzSUMobCtb/view?usp=sharing', # 9
    'https://drive.google.com/file/d/1ExzVtVEMUVOMnAdLY1qPvhZyjjdjMEm3/view?usp=sharing', # 10
    'https://drive.google.com/file/d/164gk4u3YqwwZBJqYE-Qek1aB3EhuAkFJ/view?usp=sharing', # 11
    'https://drive.google.com/file/d/1vv2fJH9iY6DDSqAqBRWbbWMP2BoWNlNG/view?usp=sharing', # 12
    'https://drive.google.com/file/d/1qIFrDyQmrlu2vKeIFmjAW9GznneNXSr0/view?usp=sharing', # 13
    'https://drive.google.com/file/d/1LqvQrTzwe2M8Jk844Vgzvin6eGRaQgdr/view?usp=sharing', # 14
    'https://drive.google.com/file/d/1ZCCibZgkG0cvmdoZbDe73dh2nTcp9ArK/view?usp=sharing', # 15
    'https://drive.google.com/file/d/1CI4dCssHITKbOl76JJWMAn5aK5IeCg3I/view?usp=sharing', # 16
    'https://drive.google.com/file/d/1f4W0ctQXxs5oiue5NmYvwrm_FzTR8mOf/view?usp=sharing', # 17
    'https://drive.google.com/file/d/1jHCpMWn2xS5kl3ObSwiJ0Vrqs2dMeDZb/view?usp=sharing', # 18
    'https://drive.google.com/file/d/1nPQ11uARfH6Y8UZBn7Hln29zYu_HLjXA/view?usp=sharing', # 19
    'https://drive.google.com/file/d/14ScRkLLiQLtqMfki7UNHrWpFQZp9cddL/view?usp=sharing', # 20
    'https://drive.google.com/file/d/1AJ50JM-QIrbf9Jn6l3hxSKOOWG0gtb9w/view?usp=sharing', # 21
    'https://drive.google.com/file/d/1Yaab4Zl4fyNQihGhB-T6e7VK5MJY-R9P/view?usp=sharing', # 22
    'https://drive.google.com/file/d/16C-Wu8rVj7TutUZ9hrd_3GZN1ANPcLm8/view?usp=sharing', # 23
]


def main():
    for idx, FILEID in enumerate(share_urls):
        FILEID = FILEID[len('https://drive.google.com/file/d/'):].split('/')[0]
        # print(FILEID)
        idx = str(idx + 1).zfill(2)
        FILENAME = f'images.part{idx}.rar'
        while(True):
            if not os.path.exists(FILENAME):
                os.system(
                    f"wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={FILEID}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p')&id={FILEID}\" -O {FILENAME} && rm -rf /tmp/cookies.txt"
                )

            if os.path.getsize(FILENAME) >= 838480922:
                break
            else:
                os.remove(FILENAME)
    os.system('unrar x -e images.part01.rar')

if __name__ == '__main__':
    main()
