from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.file.file import File

from rembg import remove
from typing import Generator, Any


class WipeoutTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        images = tool_parameters.get("input_image")

        if not images:
            yield self.create_json_message({"result": "Please provide image file"})
            return

        if not isinstance(images, list):
            yield self.create_json_message({"result": "Image list is invalid"})
            return

        for img in images:
            if isinstance(img, File):
                try:
                    if img.mime_type not in [
                        "image/jpeg", "image/png", "image/webp", "image/bmp"
                    ]:
                        yield self.create_json_message({
                            "result": f"Unsupported file type: {img.mime_type}"
                        })
                        continue

                    input_bytes = img.blob
                    output_bytes = remove(input_bytes)

                    yield self.create_blob_message(
                        output_bytes,
                        {
                            "filename": f"wipeout_{img.filename}",
                            "mime_type": "image/png",  # Output is always PNG
                            "size": len(output_bytes),
                        }
                    )
                except Exception as e:
                    yield self.create_json_message({
                        "result": f"Error processing image: {str(e)}"
                    })
                    continue
            else:
                yield self.create_json_message({
                    "result": f"Unsupported image format: {type(img)}"
                })
