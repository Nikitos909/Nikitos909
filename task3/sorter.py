import click
import os
import shutil as sh
import eyed3


@click.command()
@click.option('-s', '--src-dir', default='.', help='Source directory', show_default=True)
@click.option('-d', '--dst-dir', default='.', help='Destinition directory', show_default=True)
def sortMusic(src_dir, dst_dir):
    '''My first program.
    This program is a little tool
    sorting your music and moving it around'''
    while True:
        if os.path.isdir(src_dir):
            try:
                it = os.scandir(src_dir)
            except PermissionError:
                print(f'You do not have access to this directory {src_dir}, please try again another directory or \
                      input "quit" to exit')
                src_dir = input('Input another directory:\n')
                if src_dir == 'quit':
                    break
            else:
                with it:
                    for i in it:
                        if not i.name.startswith('.') and i.is_file() \
                        and i.name.lower().endswith('.mp3'):
                            print(i.name)
                            try:
                                audiofile = eyed3.load(i)
                                if audiofile.tag.title:
                                    title = audiofile.tag.title.replace('/', '_')
                                else:
                                    title = i.name
                                if not audiofile.tag.artist or not audiofile.tag.album:
                                    print(f'File has no tags: {i.name}')
                                    continue
                                else:
                                    artist = audiofile.tag.artist.replace('/', '_')
                                    album = audiofile.tag.album.replace('/', '_')
                                audiofile.tag.save()
                            except PermissionError:
                                print(f'You do not have access to this file: {i.name}')
                            except AttributeError:
                                print(f'File is incorrect: {i.name}')
                                continue
                            else:
                                new_file_name = f'{title} - {artist} - {album}.mp3'
                                if os.path.exists(os.path.join(dst_dir, artist, album)):
                                    sh.move(os.path.join(src_dir, i.name), os.path.join(dst_dir, artist, album, new_file_name))
                                else:
                                    try:
                                        os.makedirs(os.path.join(dst_dir, artist, album, new_file_name))
                                    except PermissionError:
                                        print(f'You do not have access to this directory')
                                        dst_dir = input('Please input new path or input "quit":\n')
                                        if dst_dir == 'quit':
                                            break
                                    else:
                                        sh.move(os.path.join(src_dir, i.name), os.path.join(dst_dir, artist, album,
                                                                                   new_file_name))
                                print(f'Remove file from {os.path.join(src_dir, i.name)} -> to \
                                  {os.path.join(dst_dir, artist, album, new_file_name)}')
            print('Work done!')
            break
        else:
            print(f'Such {src_dir} directory is not fount')
            src_dir = input('Please input new directory or input "quit":\n')
            if src_dir == 'quit':
                break       
        
        
if __name__ == '__main__':
    sortMusic()