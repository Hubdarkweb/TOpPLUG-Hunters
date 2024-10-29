
import marshal
import zlib
import base64

# Decode, decompress, and load the original script
code = base64.b64decode('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')
code = zlib.decompress(code)
code = marshal.loads(code)

# Execute the loaded code
exec(code)
