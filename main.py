from lake_counter import LakeCounter

if __name__ == '__main__':
    example_map = [
        [0,1,1,0,0,1,1,0],
        [0,0,0,0,1,1,0,0],
        [0,1,1,1,1,1,1,1]
    ]
    correct_lake_count = 2

    print("Used map:")
    for row in example_map:
        print(row)
    print("Correct lake count:", correct_lake_count)
    lake_counter = LakeCounter()
    count = lake_counter.count_lakes(example_map)
    print(f"Function output: {count}, identical to correct value: {count == correct_lake_count}")