import wikipedia


def search(root, target):
    root = wikipedia.check(root)
    target = wikipedia.check(target)
    if root and target:
        if root != target:
            visited = set([root])
            queue = [[root]]
            found = False
            print("Finding the shortest route from '{}' to '{}'...".format(root, target))
            while queue and not found:
                try:
                    path = queue[0]
                    current = path[-1]
                    print(" > ".join(path))
                    queue = queue[1:]
                    nodes = wikipedia.get_links(current)
                    for node in nodes:
                        if node not in visited:
                            if node == target:
                                result = path + [node]
                                found = True
                            visited.add(node)
                            new_path = path + [node]
                            queue.append(new_path)
                except KeyboardInterrupt:
                    exit("Keyboard Interrupt")
            
            if found:
                print("Shortest path: ")
                print(" > ".join(result))
            else:
                print("No possible route")

        else:
            print("Root and target are same")


start = input("Page to start at: ")
if start == "?":
    start, end = wikipedia.random(2)
else:
    end = input("Page to find: ")
search(start, end)

