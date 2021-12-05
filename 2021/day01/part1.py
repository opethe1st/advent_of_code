if __name__ == "__main__":
    depths = [int(depth) for depth in open("input.txt")]
    print(sum(next_depth > depth for depth, next_depth in zip(depths, depths[1:])))
