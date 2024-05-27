def TOH(N, start, aux, dest):
    if N == 1:
        print(f"move disk 1 from rod {start} to rod {dest}")
        return
    TOH(N - 1, start, dest, aux)
    print(f"move disk {N} from rod {start} to rod {dest}")
    TOH(N - 1, aux, start, dest)

disk = 4
TOH(disk, "A", "B", "C")
