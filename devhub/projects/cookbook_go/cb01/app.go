// Read a file on Google Drive and print meta information
package main

import (
	"context"
	"fmt"

	"google.golang.org/api/drive/v3"
)

func main() {
	// Create a Drive service client.
	ctx := context.Background()
	srv, err := drive.NewService(ctx)
	if err != nil {
		fmt.Printf("Unable to create Drive client: %v\n", err)
		return
	}

	// Get the file ID.
	fileId := "YOUR_FILE_ID" // Replace with the actual file ID

	// Retrieve the file metadata.
	file, err := srv.Files.Get(fileId).Fields("id, name, mimeType, size, createdTime, modifiedTime").Do()
	if err != nil {
		fmt.Printf("Unable to retrieve file metadata: %v\n", err)
		return
	}

	// Print the file metadata.
	fmt.Printf("File ID: %s\n", file.Id)
	fmt.Printf("File Name: %s\n", file.Name)
	fmt.Printf("File MimeType: %s\n", file.MimeType)
	fmt.Printf("File Size: %d bytes\n", file.Size)
	fmt.Printf("File Created Time: %s\n", file.CreatedTime)
	fmt.Printf("File Modified Time: %s\n", file.ModifiedTime)

	// Download the file content (optional).
	if _, err := srv.Files.Get(fileId).Download(ctx); err != nil {
		fmt.Printf("Unable to download file content: %v\n", err)
		return
	}
	fmt.Println("File content downloaded successfully.")
}
