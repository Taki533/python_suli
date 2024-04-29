# UnPKG rev 0x00000008 (public edition), (c) flatz
 
import sys, os, hashlib, hmac, struct, math, traceback
from cStringIO import StringIO
 
# parse arguments
 
if len(sys.argv) < 3:
    script_file_name = os.path.split(sys.argv[0])[1]
    print ('usage: {0} <pkg file> <output dir>').format(script_file_name)
    sys.exit()
 
pkg_file_path = sys.argv[1]
if not os.path.isfile(pkg_file_path):
    print ('error: invalid file specified')
    sys.exit()
 
output_dir = sys.argv[2]
if os.path.exists(output_dir) and not os.path.isdir(output_dir):
    print ('error: invalid directory specified')
    sys.exit()
elif not os.path.exists(output_dir):
    os.makedirs(output_dir)
 
# cryptography functions
 
def sha256(data):
    return hashlib.sha256(data).digest()
 
# utility functions
 
uint64_fmt, uint32_fmt, uint16_fmt, uint8_fmt = '>Q', '>I', '>H', '>B'
int64_fmt, int32_fmt, int16_fmt, int8_fmt = '>q', '>i', '>h', '>b'
 
def read_string(f, length):
    return f.read(length)
def read_cstring(f):
    s = ''
    while True:
        c = f.read(1)
        if not c:
            return False
        if ord(c) == 0:
            break
        s += c
    return s
 
def read_uint8_le(f):
    return struct.unpack('<B', f.read(struct.calcsize('<B')))[0]
def read_uint8_be(f):
    return struct.unpack('>B', f.read(struct.calcsize('>B')))[0]
def read_uint16_le(f):
    return struct.unpack('<H', f.read(struct.calcsize('<H')))[0]
def read_uint16_be(f):
    return struct.unpack('>H', f.read(struct.calcsize('>H')))[0]
def read_uint32_le(f):
    return struct.unpack('<I', f.read(struct.calcsize('<I')))[0]
def read_uint32_be(f):
    return struct.unpack('>I', f.read(struct.calcsize('>I')))[0]
def read_uint64_le(f):
    return struct.unpack('<Q', f.read(struct.calcsize('<Q')))[0]
def read_uint64_be(f):
    return struct.unpack('>Q', f.read(struct.calcsize('>Q')))[0]
def read_int8_le(f):
    return struct.unpack('<b', f.read(struct.calcsize('<b')))[0]
def read_int8_be(f):
    return struct.unpack('>b', f.read(struct.calcsize('>b')))[0]
def read_int16_le(f):
    return struct.unpack('<h', f.read(struct.calcsize('<h')))[0]
def read_int16_be(f):
    return struct.unpack('>h', f.read(struct.calcsize('>h')))[0]
def read_int32_le(f):
    return struct.unpack('<i', f.read(struct.calcsize('<i')))[0]
def read_int32_be(f):
    return struct.unpack('>i', f.read(struct.calcsize('>i')))[0]
def read_int64_le(f):
    return struct.unpack('<q', f.read(struct.calcsize('<q')))[0]
def read_int64_be(f):
    return struct.unpack('>q', f.read(struct.calcsize('>q')))[0]
 
# main code
 
PKG_MAGIC = '\x7FCNT'
CONTENT_ID_SIZE = 0x24
SHA256_HASH_SIZE = 0x20
META_ENTRY_SIZE = 0x20
 
FILE_TYPE_FLAGS_RETAIL = 1 << 31
 
ENTRY_TYPE_DIGEST_TABLE = 0x0001
ENTRY_TYPE_0x800        = 0x0010
ENTRY_TYPE_0x200        = 0x0020
ENTRY_TYPE_0x180        = 0x0080
ENTRY_TYPE_META_TABLE   = 0x0100
ENTRY_TYPE_NAME_TABLE   = 0x0200
 
ENTRY_TYPE_LICENSE = 0x04
ENTRY_TYPE_FILE1   = 0x10
ENTRY_TYPE_FILE2   = 0x12
 
ENTRY_TABLE_MAP = {
    ENTRY_TYPE_DIGEST_TABLE: '.digests',
    ENTRY_TYPE_0x800: '.entry_0x800',
    ENTRY_TYPE_0x200: '.entry_0x200',
    ENTRY_TYPE_0x180: '.entry_0x180',
    ENTRY_TYPE_META_TABLE: '.meta',
    ENTRY_TYPE_NAME_TABLE: '.names',
 
    0x0400: 'license.dat',
    0x0401: 'license.info',
    0x1000: 'param.sfo',
    0x1001: 'playgo-chunk.dat',
    0x1002: 'playgo-chunk.sha',
    0x1003: 'playgo-manifest.xml',
    0x1004: 'pronunciation.xml',
    0x1005: 'pronunciation.sig',
    0x1006: 'pic1.png',
    0x1008: 'app/playgo-chunk.dat',
    0x1200: 'icon0.png',
    0x1220: 'pic0.png',
    0x1240: 'snd0.at9',
    0x1260: 'changeinfo/changeinfo.xml',
}
 
class MyError(Exception):
    def __init__(self, message):
        self.message = message
 
    def __str__(self):
        return repr(self.message)
 
class FileTableEntry:
    entry_fmt = '>IIIIII8x'
 
    def __init__(self):
        pass
 
    def read(self, f):
        self.type, self.unk1, self.flags1, self.flags2, self.offset, self.size = struct.unpack(self.entry_fmt, f.read(struct.calcsize(self.entry_fmt)))
        self.key_index = (self.flags2 & 0xF000) >> 12
        self.name = None
 
try:
    with open(pkg_file_path, 'rb') as pkg_file:
        magic = read_string(pkg_file, 4)
        if magic != PKG_MAGIC:
            raise MyError('invalid file magic')
 
        type = read_uint32_be(pkg_file)
        is_retail = (type & FILE_TYPE_FLAGS_RETAIL) != 0
 
        pkg_file.seek(0x10) # FIXME: or maybe uint16 at 0x16???
        num_table_entries = read_uint32_be(pkg_file)
 
        pkg_file.seek(0x14)
        num_system_entries = read_uint16_be(pkg_file)
 
        pkg_file.seek(0x18)
        file_table_offset = read_uint32_be(pkg_file)
 
        pkg_file.seek(0x1C)
        main_entries_data_size = read_uint32_be(pkg_file)
 
        pkg_file.seek(0x24)
        body_offset = read_uint32_be(pkg_file)
        pkg_file.seek(0x2C)
        body_size = read_uint32_be(pkg_file)
 
        pkg_file.seek(0x414)
        content_offset = read_uint32_be(pkg_file)
        pkg_file.seek(0x41C)
        content_size = read_uint32_be(pkg_file)
 
        pkg_file.seek(0x40)
        content_id = read_cstring(pkg_file)
        if len(content_id) != CONTENT_ID_SIZE:
            raise MyError('invalid content id')
 
        pkg_file.seek(0x100)
        main_entries1_digest = pkg_file.read(SHA256_HASH_SIZE)
        main_entries2_digest = pkg_file.read(SHA256_HASH_SIZE)
        digest_table_digest = pkg_file.read(SHA256_HASH_SIZE)
        body_digest = pkg_file.read(SHA256_HASH_SIZE)
 
        pkg_file.seek(0x440)
        content_digest = pkg_file.read(SHA256_HASH_SIZE)
        content_one_block_digest = pkg_file.read(SHA256_HASH_SIZE)
 
        table_entries = []
        table_entries_map = {}
        pkg_file.seek(file_table_offset)
        for i in xrange(num_table_entries):
            entry = FileTableEntry()
            entry.read(pkg_file)
            table_entries_map[entry.type] = len(table_entries)
            table_entries.append(entry)
 
        entry_names = None
        entry_digests = None
        for i in xrange(num_table_entries):
            entry = table_entries[i]
            if entry.type == ENTRY_TYPE_NAME_TABLE:
                pkg_file.seek(entry.offset)
                data = pkg_file.read(entry.size)
                if data and len(data) > 0:
                    data = StringIO(data)
                    entry_names = []
                    c = data.read(1)
                    if ord(c) == 0:
                        while True:
                            name = read_cstring(data)
                            if not name:
                                break
                            entry_names.append(name)
                    else:
                        raise MyError('weird name table format')
                break
        entry_name_index = 0
        for i in xrange(num_table_entries):
            entry = table_entries[i]
            type, index = (entry.type >> 8) & 0xFF, entry.type & 0xFF
            if type == ENTRY_TYPE_FILE1 or type == ENTRY_TYPE_FILE2:
                if entry_name_index < len(entry_names):
                    entry.name = entry_names[entry_name_index]
                    entry_name_index += 1
                else:
                    raise MyError('entry name index out of bounds')
            elif entry.type in ENTRY_TABLE_MAP:
                entry.name = ENTRY_TABLE_MAP[entry.type]
            if entry.type == ENTRY_TYPE_DIGEST_TABLE and entry_digests is None:
                pkg_file.seek(entry.offset)
                entry_digests = pkg_file.read(entry.size)
 
        data = ''
        for entry_type in [ENTRY_TYPE_0x800, ENTRY_TYPE_0x200, ENTRY_TYPE_0x180, ENTRY_TYPE_META_TABLE, ENTRY_TYPE_DIGEST_TABLE]:
            entry = table_entries[table_entries_map[entry_type]]
            pkg_file.seek(entry.offset)
            data += pkg_file.read(entry.size)
        computed_main_entries1_digest = sha256(data)
 
        data = ''
        for entry_type in [ENTRY_TYPE_0x800, ENTRY_TYPE_0x200, ENTRY_TYPE_0x180, ENTRY_TYPE_META_TABLE]:
            entry = table_entries[table_entries_map[entry_type]]
            pkg_file.seek(entry.offset)
            size = entry.size if entry_type != ENTRY_TYPE_META_TABLE else num_system_entries * META_ENTRY_SIZE
            data += pkg_file.read(size)
        computed_main_entries2_digest = sha256(data)
 
        entry = table_entries[table_entries_map[ENTRY_TYPE_DIGEST_TABLE]]
        pkg_file.seek(entry.offset)
        data = pkg_file.read(entry.size)
        computed_digest_table_digest = sha256(data)
 
        pkg_file.seek(body_offset)
        body = pkg_file.read(body_size)
        computed_body_digest = sha256(body)
 
        computed_entry_digests = '\x00' * SHA256_HASH_SIZE
        for i in xrange(num_table_entries):
            entry = table_entries[i]
            if entry.type == ENTRY_TYPE_DIGEST_TABLE:
                continue
            pkg_file.seek(entry.offset)
            data = pkg_file.read(entry.size)
            computed_entry_digests += sha256(data)
 
        for i in xrange(num_table_entries):
            entry = table_entries[i]
            name = entry.name if entry.name is not None else 'entry_{0:03}.bin'.format(i)
            file_path = os.path.join(output_dir, name)
            file_dir = os.path.split(file_path)[0]
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            with open(file_path, 'wb') as entry_file:
                pkg_file.seek(entry.offset)
                data = pkg_file.read(entry.size)
                entry_file.write(data)
 
        block_size = 0x10000
        num_blocks = 1 + int((content_size - 1) / block_size) if content_size > 0 else 0
 
        pkg_file.seek(content_offset)
        data = pkg_file.read(block_size)
        computed_content_one_block_digest = sha256(data)
 
        hash_context = hashlib.sha256()
        pkg_file.seek(content_offset)
        bytes_left = content_size
        for i in xrange(num_blocks):
            current_size = block_size if bytes_left > block_size else bytes_left
            data = pkg_file.read(current_size)
            hash_context.update(data)
            bytes_left -= block_size
        computed_content_digest = hash_context.digest()
 
        is_digests_valid = computed_main_entries1_digest == main_entries1_digest
        is_digests_valid = is_digests_valid and computed_main_entries2_digest == main_entries2_digest
        is_digests_valid = is_digests_valid and computed_digest_table_digest == digest_table_digest
        is_digests_valid = is_digests_valid and computed_body_digest == body_digest
        is_digests_valid = is_digests_valid and computed_entry_digests == entry_digests
        is_digests_valid = is_digests_valid and computed_content_digest == content_digest
        is_digests_valid = is_digests_valid and computed_content_one_block_digest == content_one_block_digest
 
        print ('File information:')
        print ('             Magic: 0x{0}'.format(magic.encode('hex').upper()))
        print ('              Type: 0x{0:08X}'.format(type), '(retail)' if is_retail else '')
        print ('        Content ID: {0}'.format(content_id))
        print (' Num table entries: {0}'.format(num_table_entries))
        print ('Entry table offset: 0x{0:08X}'.format(file_table_offset))
        print ('     Digest status: {0}'.format('OK' if is_digests_valid else 'FAIL'))
        print()
 
        if num_table_entries > 0:
            print ('Table entries:')
            for i in xrange(num_table_entries):
                entry = table_entries[i]
                print ('  Entry #{0:03}:'.format(i))
                print ('         Type: 0x{0:08X}'.format(entry.type))
                print ('         Unk1: 0x{0:08X}'.format(entry.unk1))
                if entry.name is not None:
                    print ('         Name: {0}'.format(entry.name))
                print ('       Offset: 0x{0:08X}'.format(entry.offset))
                print ('         Size: 0x{0:08X}'.format(entry.size))
                print ('      Flags 1: 0x{0:08X}'.format(entry.flags1))
                print ('      Flags 2: 0x{0:08X}'.format(entry.flags2))
                print ('    Key index: {0}'.format('N/A' if entry.key_index == 0 else entry.key_index))
            print
 
except IOError:
    print ('error: i/o error during processing')
except MyError as e:
    print ('error: {0}', e.message)
except:
    print ('error: unexpected error:'), sys.exc_info()[0]
    traceback.print_exc(file=sys.stdout)