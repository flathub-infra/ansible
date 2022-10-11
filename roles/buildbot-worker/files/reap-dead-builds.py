#!/usr/bin/env python3
import psutil


def main():
    for proc in psutil.process_iter():
        if proc.name() == "flatpak-bwrap":
            children = proc.children()
            if len(children) == 1 and children[0].name() == "rofiles-fuse":
                children[0].kill()


if __name__ == "__main__":
    main()
