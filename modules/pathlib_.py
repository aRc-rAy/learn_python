from pathlib import Path

path=Path(__file__)

# get details of the path
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

print(f"Path is at {path.absolute()}")


print("\nChecking path properties:")
if path.exists():
    print("Path exists!")
if path.is_file():
    print("It's a file!")
if path.is_dir():
    print("It's a directory!")
    

print("\nCreating a new directory:")
new_dir=path.parent/"created_by_pathlib"
new_dir.mkdir(exist_ok=True)
print(f"Created directory: {new_dir.absolute()}")

print("\nCreating a new file:")
new_file=new_dir/"test.txt"
new_file.touch(exist_ok=True)
print(f"Created file: {new_file.absolute()}")

print("\nWriting to the file:")
with new_file.open("a") as f:
    f.write("\nHello, World!")
print(f"Written to file: {new_file.absolute()}")

print("\nReading from the file:")
with new_file.open("r") as f:
    content = f.read()
print(f"Content of file: {content}")
print(f"Read from file: {new_file.absolute()}")

print("\nDeleting the file:")
# new_file.unlink(missing_ok=True)
print(f"Deleted file: {new_file.absolute()}")

print("\nDeleting the directory:")
# new_dir.rmdir()
print(f"Deleted directory: {new_dir.absolute()}")

