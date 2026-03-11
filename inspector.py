import os

# Ask user for directory path
path = input("Enter folder path: ")

# Validate that the path exists
if not os.path.exists(path):
    print("Invalid path")
    exit()

# Ensure the path is a directory (not a file)
if not os.path.isdir(path):
    print("Given path is not a folder")
    exit()

print("===== DIRECTORY INSPECTOR =====")
print("\nScanning:", path)
print()

# Counters and trackers
file_count = 0
folder_count = 0
total_size = 0

# Dictionary to group files by extension
file_types = {}

# List to store folder names
folders = []

# Track the largest file
largest_file_name = None
largest_file_size = 0


# Scan directory entries
for entry in os.scandir(path):

    # Handle files
    if entry.is_file():

        file_count += 1

        # Get file size
        size = os.path.getsize(entry.path)
        total_size += size

        name = entry.name

        # Detect file extension
        if "." in name:
            ext = name.split(".")[-1].lower()
        else:
            ext = "no_extension"

        # Add file to extension group
        if ext not in file_types:
            file_types[ext] = []

        file_types[ext].append((name, size))

        # Check if this is the largest file so far
        if size > largest_file_size:
            largest_file_size = size
            largest_file_name = name

    # Handle folders
    elif entry.is_dir():

        folder_count += 1
        folders.append(entry.name)


print("FILES")
print("-----")

# Print files grouped by extension (sorted for clean output)
for ext in sorted(file_types):

    if ext == "no_extension":
        print("\n(no extension) files:")
    else:
        print(f"\n.{ext} files:")

    for name, size in file_types[ext]:

        # Convert size to KB if needed
        if size >= 1024:
            size_kb = size / 1024
            print(f"{name} - {size_kb:.2f} KB")
        else:
            print(f"{name} - {size} bytes")


print("\nFOLDERS")
print("-------")

# Print folder names
for folder in sorted(folders):
    print(folder)


print("\nSUMMARY")
print("-------")

print("Total files:", file_count)
print("Total folders:", folder_count)

# Show total size
if total_size >= 1024:
    print("Total size:", f"{total_size/1024:.2f}", "KB")
else:
    print("Total size:", total_size, "bytes")


print("\nLargest file")
print("------------")

# Display largest file info
if largest_file_name:
    if largest_file_size >= 1024:
        print(f"{largest_file_name} - {largest_file_size/1024:.2f} KB")
    else:
        print(f"{largest_file_name} - {largest_file_size} bytes")
else:
    print("No files found")
