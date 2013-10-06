'''Wrapper for lms2012.h

Generated with:
./ctypesgen.py -a -I /home/pikachu/arm-2009q1/arm-none-linux-gnueabi/libc/usr/includ -o /home/pikachu/ev3/python-ev3/ev3/cdriver/lms2012.py --cpp=/home/pikachu/arm-2009q1/bin/arm-none-linux-gnueabi-gcc -E /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 17
for _lib in _libs.values():
    try:
        __s8 = (c_char).in_dll(_lib, '__s8')
        break
    except:
        pass

__u8 = c_ubyte # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 18

__u16 = c_ushort # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 21

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 23
for _lib in _libs.values():
    try:
        __s32 = (c_int).in_dll(_lib, '__s32')
        break
    except:
        pass

__u32 = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 24

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 30
for _lib in _libs.values():
    try:
        __s64 = (c_long).in_dll(_lib, '__s64')
        break
    except:
        pass

__u64 = c_ulonglong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 31

umode_t = c_ushort # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/types.h: 8

UBYTE = c_ubyte # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 29

UWORD = c_ushort # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 30

ULONG = c_uint # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 31

SBYTE = c_byte # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 33

SWORD = c_short # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 34

SLONG = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 35

FLOAT = c_float # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 37

DATA8 = SBYTE # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 61

DATA16 = SWORD # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 62

DATA32 = SLONG # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 63

DATAF = FLOAT # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 64

VARDATA = UBYTE # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 68

IMGDATA = UBYTE # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 69

PRGID = UWORD # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 71

OBJID = UWORD # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 73

IP = POINTER(IMGDATA) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 74

LP = POINTER(VARDATA) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 75

GP = POINTER(VARDATA) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 76

IMINDEX = ULONG # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 78

GBINDEX = ULONG # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 79

LBINDEX = ULONG # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 80

TRIGGER = UWORD # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 81

PARS = UBYTE # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 82

IMOFFS = SLONG # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 83

HANDLER = DATA16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 85

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 152
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'Sign',
    'ImageSize',
    'VersionInfo',
    'NumberOfObjects',
    'GlobalBytes',
]
struct_anon_1._fields_ = [
    ('Sign', UBYTE * 4),
    ('ImageSize', IMINDEX),
    ('VersionInfo', UWORD),
    ('NumberOfObjects', OBJID),
    ('GlobalBytes', GBINDEX),
]

IMGHEAD = struct_anon_1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 152

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 174
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'OffsetToInstructions',
    'OwnerObjectId',
    'TriggerCount',
    'LocalBytes',
]
struct_anon_2._fields_ = [
    ('OffsetToInstructions', IP),
    ('OwnerObjectId', OBJID),
    ('TriggerCount', TRIGGER),
    ('LocalBytes', LBINDEX),
]

OBJHEAD = struct_anon_2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 174

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 184
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'Addr',
]
struct_anon_3._fields_ = [
    ('Addr', IMINDEX),
]

LABEL = struct_anon_3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lmstypes.h: 184

enum_anon_4 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opERROR = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opNOP = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPROGRAM_STOP = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPROGRAM_START = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOBJECT_STOP = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOBJECT_START = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOBJECT_TRIG = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOBJECT_WAIT = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opRETURN = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCALL = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOBJECT_END = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSLEEP = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPROGRAM_INFO = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opLABEL = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPROBE = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opDO = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opADD8 = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opADD16 = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opADD32 = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opADDF = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSUB8 = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSUB16 = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSUB32 = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSUBF = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMUL8 = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMUL16 = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMUL32 = 26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMULF = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opDIV8 = 28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opDIV16 = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opDIV32 = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opDIVF = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOR8 = 32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOR16 = 33 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOR32 = 34 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opAND8 = 36 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opAND16 = 37 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opAND32 = 38 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opXOR8 = 40 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opXOR16 = 41 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opXOR32 = 42 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opRL8 = 44 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opRL16 = 45 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opRL32 = 46 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINIT_BYTES = 47 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE8_8 = 48 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE8_16 = 49 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE8_32 = 50 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE8_F = 51 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE16_8 = 52 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE16_16 = 53 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE16_32 = 54 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE16_F = 55 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE32_8 = 56 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE32_16 = 57 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE32_32 = 58 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVE32_F = 59 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVEF_8 = 60 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVEF_16 = 61 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVEF_32 = 62 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMOVEF_F = 63 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR = 64 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_FALSE = 65 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_TRUE = 66 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_NAN = 67 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LT8 = 68 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LT16 = 69 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LT32 = 70 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LTF = 71 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GT8 = 72 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GT16 = 73 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GT32 = 74 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GTF = 75 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_EQ8 = 76 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_EQ16 = 77 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_EQ32 = 78 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_EQF = 79 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_NEQ8 = 80 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_NEQ16 = 81 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_NEQ32 = 82 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_NEQF = 83 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LTEQ8 = 84 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LTEQ16 = 85 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LTEQ32 = 86 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_LTEQF = 87 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GTEQ8 = 88 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GTEQ16 = 89 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GTEQ32 = 90 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCP_GTEQF = 91 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSELECT8 = 92 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSELECT16 = 93 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSELECT32 = 94 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSELECTF = 95 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSYSTEM = 96 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPORT_CNV_OUTPUT = 97 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opPORT_CNV_INPUT = 98 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opNOTE_TO_FREQ = 99 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LT8 = 100 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LT16 = 101 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LT32 = 102 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LTF = 103 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GT8 = 104 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GT16 = 105 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GT32 = 106 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GTF = 107 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_EQ8 = 108 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_EQ16 = 109 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_EQ32 = 110 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_EQF = 111 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_NEQ8 = 112 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_NEQ16 = 113 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_NEQ32 = 114 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_NEQF = 115 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LTEQ8 = 116 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LTEQ16 = 117 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LTEQ32 = 118 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_LTEQF = 119 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GTEQ8 = 120 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GTEQ16 = 121 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GTEQ32 = 122 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opJR_GTEQF = 123 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINFO = 124 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSTRINGS = 125 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMEMORY_WRITE = 126 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMEMORY_READ = 127 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opUI_FLUSH = 128 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opUI_READ = 129 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opUI_WRITE = 130 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opUI_BUTTON = 131 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opUI_DRAW = 132 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opTIMER_WAIT = 133 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opTIMER_READY = 134 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opTIMER_READ = 135 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opBP0 = 136 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opBP1 = 137 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opBP2 = 138 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opBP3 = 139 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opBP_SET = 140 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMATH = 141 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opRANDOM = 142 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opTIMER_READ_US = 143 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opKEEP_ALIVE = 144 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_READ = 145 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_WRITE = 146 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSOUND = 148 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSOUND_TEST = 149 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opSOUND_READY = 150 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_SAMPLE = 151 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_DEVICE_LIST = 152 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_DEVICE = 153 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_READ = 154 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_TEST = 155 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_READY = 156 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_READSI = 157 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_READEXT = 158 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opINPUT_WRITE = 159 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_GET_TYPE = 160 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_SET_TYPE = 161 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_RESET = 162 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_STOP = 163 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_POWER = 164 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_SPEED = 165 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_START = 166 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_POLARITY = 167 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_READ = 168 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_TEST = 169 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_READY = 170 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_POSITION = 171 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_STEP_POWER = 172 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_TIME_POWER = 173 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_STEP_SPEED = 174 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_TIME_SPEED = 175 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_STEP_SYNC = 176 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_TIME_SYNC = 177 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_CLR_COUNT = 178 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_GET_COUNT = 179 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opOUTPUT_PRG_STOP = 180 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opFILE = 192 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opARRAY = 193 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opARRAY_WRITE = 194 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opARRAY_READ = 195 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opARRAY_APPEND = 196 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMEMORY_USAGE = 197 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opFILENAME = 198 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opREAD8 = 200 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opREAD16 = 201 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opREAD32 = 202 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opREADF = 203 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opWRITE8 = 204 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opWRITE16 = 205 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opWRITE32 = 206 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opWRITEF = 207 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_READY = 208 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_READDATA = 209 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_WRITEDATA = 210 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_GET = 211 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_SET = 212 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_TEST = 213 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_REMOVE = 214 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opCOM_WRITEFILE = 215 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_OPEN = 216 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_WRITE = 217 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_READ = 218 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_TEST = 219 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_READY = 220 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opMAILBOX_CLOSE = 221 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

opTST = 255 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

OP = enum_anon_4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 456

enum_anon_5 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_VBATT = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_IBATT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_OS_VERS = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_EVENT = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_TBATT = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_IINT = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_IMOTOR = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_STRING = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_HW_VERS = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_FW_VERS = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_FW_BUILD = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_OS_BUILD = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_ADDRESS = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_CODE = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

KEY = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_SHUTDOWN = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_WARNING = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_LBATT = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

TEXTBOX_READ = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_VERSION = 26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_IP = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_POWER = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_SDCARD = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

GET_USBSTICK = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

UI_READ_SUBCODES = (GET_USBSTICK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

UI_READ_SUBCODE = enum_anon_5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 497

enum_anon_6 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

WRITE_FLUSH = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

FLOATVALUE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

STAMP = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

PUT_STRING = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

VALUE8 = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

VALUE16 = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

VALUE32 = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

VALUEF = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

ADDRESS = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

CODE = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

DOWNLOAD_END = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

SCREEN_BLOCK = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

TEXTBOX_APPEND = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

SET_BUSY = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

SET_TESTPIN = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

INIT_RUN = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

UPDATE_RUN = 26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

LED = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

POWER = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

GRAPH_SAMPLE = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

TERMINAL = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

UI_WRITE_SUBCODES = (TERMINAL + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

UI_WRITE_SUBCODE = enum_anon_6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 534

enum_anon_7 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

SHORTPRESS = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

LONGPRESS = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

WAIT_FOR_PRESS = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

FLUSH = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

PRESS = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

RELEASE = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

GET_HORZ = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

GET_VERT = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

PRESSED = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

SET_BACK_BLOCK = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

GET_BACK_BLOCK = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

TESTSHORTPRESS = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

TESTLONGPRESS = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

GET_BUMBED = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

GET_CLICK = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

UI_BUTTON_SUBCODES = (GET_CLICK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

UI_BUTTON_SUBCODE = enum_anon_7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 565

enum_anon_8 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 582

COMMAND = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 582

COM_READ_SUBCODES = (COMMAND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 582

COM_READ_SUBCODE = enum_anon_8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 582

enum_anon_9 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 599

REPLY = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 599

COM_WRITE_SUBCODES = (REPLY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 599

COM_WRITE_SUBCODE = enum_anon_9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 599

enum_anon_10 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_ON_OFF = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_VISIBLE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_RESULT = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_PIN = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

SEARCH_ITEMS = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

SEARCH_ITEM = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

FAVOUR_ITEMS = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

FAVOUR_ITEM = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_ID = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_BRICKNAME = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_NETWORK = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_PRESENT = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_ENCRYPT = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

CONNEC_ITEMS = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

CONNEC_ITEM = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_INCOMING = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

GET_MODE2 = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

COM_GET_SUBCODES = (GET_MODE2 + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

COM_GET_SUBCODE = enum_anon_10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 631

enum_anon_11 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_ON_OFF = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_VISIBLE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_SEARCH = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_PIN = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_PASSKEY = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_CONNECTION = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_BRICKNAME = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_MOVEUP = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_MOVEDOWN = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_ENCRYPT = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_SSID = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

SET_MODE2 = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

COM_SET_SUBCODES = (SET_MODE2 + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

COM_SET_SUBCODE = enum_anon_11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 658

enum_anon_12 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_FORMAT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CAL_MINMAX = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CAL_DEFAULT = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_TYPEMODE = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_SYMBOL = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CAL_MIN = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CAL_MAX = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

SETUP = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CLR_ALL = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_RAW = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_CONNECTION = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

STOP_ALL = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_NAME = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_MODENAME = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

SET_RAW = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_FIGURES = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_CHANGES = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

CLR_CHANGES = 26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

READY_PCT = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

READY_RAW = 28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

READY_SI = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_MINMAX = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

GET_BUMPS = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

INPUT_DEVICESUBCODES = (GET_BUMPS + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

INPUT_DEVICE_SUBCODE = enum_anon_12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 697

enum_anon_13 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

OBJ_STOP = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

OBJ_START = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

GET_STATUS = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

GET_SPEED = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

GET_PRGRESULT = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

SET_INSTR = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

PROGRAM_INFO_SUBCODES = (SET_INSTR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

PROGRAM_INFO_SUBCODE = enum_anon_13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 719

enum_anon_14 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

UPDATE = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

CLEAN = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

PIXEL = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

LINE = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

CIRCLE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

TEXT = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

ICON = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

PICTURE = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

VALUE = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

FILLRECT = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

RECT = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

NOTIFICATION = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

QUESTION = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

KEYBOARD = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

BROWSE = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

VERTBAR = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

INVERSERECT = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

SELECT_FONT = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

TOPLINE = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

FILLWINDOW = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

SCROLL = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

DOTLINE = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

VIEW_VALUE = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

VIEW_UNIT = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

FILLCIRCLE = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

STORE = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

RESTORE = 26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

ICON_QUESTION = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

BMPFILE = 28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

POPUP = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

GRAPH_SETUP = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

GRAPH_DRAW = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

TEXTBOX = 32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

UI_DRAW_SUBCODES = (TEXTBOX + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

UI_DRAW_SUBCODE = enum_anon_14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 768

enum_anon_15 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

OPEN_APPEND = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

OPEN_READ = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

OPEN_WRITE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

READ_VALUE = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

WRITE_VALUE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

READ_TEXT = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

WRITE_TEXT = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

CLOSE = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

LOAD_IMAGE = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_HANDLE = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

MAKE_FOLDER = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_POOL = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

SET_LOG_SYNC_TIME = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_FOLDERS = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_LOG_SYNC_TIME = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_SUBFOLDER_NAME = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

WRITE_LOG = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

CLOSE_LOG = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_IMAGE = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_ITEM = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_CACHE_FILES = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

PUT_CACHE_FILE = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_CACHE_FILE = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

DEL_CACHE_FILE = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

DEL_SUBFOLDER = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

GET_LOG_NAME = 25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

OPEN_LOG = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

READ_BYTES = 28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

WRITE_BYTES = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

REMOVE = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

MOVE = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

FILE_SUBCODES = (MOVE + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

FILE_SUBCODE = enum_anon_15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 816

enum_anon_16 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

DELETE = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

CREATE8 = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

CREATE16 = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

CREATE32 = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

CREATEF = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

RESIZE = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

FILL = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

COPY = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

INIT8 = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

INIT16 = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

INIT32 = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

INITF = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

SIZE = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

READ_CONTENT = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

WRITE_CONTENT = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

READ_SIZE = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

ARRAY_SUBCODES = (READ_SIZE + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

ARRAY_SUBCODE = enum_anon_16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 848

enum_anon_17 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

EXIST = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

TOTALSIZE = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

SPLIT = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

MERGE = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

CHECK = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

PACK = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

UNPACK = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

GET_FOLDERNAME = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

FILENAME_SUBCODES = (GET_FOLDERNAME + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

FILENAME_SUBCODE = enum_anon_17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 871

enum_anon_18 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

SET_ERROR = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

GET_ERROR = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

ERRORTEXT = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

GET_VOLUME = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

SET_VOLUME = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

GET_MINUTES = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

SET_MINUTES = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

INFO_SUBCODES = (SET_MINUTES + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

INFO_SUBCODE = enum_anon_18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 895

enum_anon_19 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

BREAK = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

TONE = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

PLAY = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

REPEAT = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

SERVICE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

SOUND_SUBCODES = (SERVICE + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

SOUND_SUBCODE = enum_anon_19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 916

enum_anon_20 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

GET_SIZE = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

ADD = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

COMPARE = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

DUPLICATE = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

VALUE_TO_STRING = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

STRING_TO_VALUE = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

STRIP = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

NUMBER_TO_STRING = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

SUB = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

VALUE_FORMATTED = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

NUMBER_FORMATTED = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

STRING_SUBCODES = (NUMBER_FORMATTED + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

STRING_SUBCODE = enum_anon_20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 943

enum_anon_21 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

GUI_SLOT = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

USER_SLOT = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

CMD_SLOT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

TERM_SLOT = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

DEBUG_SLOT = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

SLOTS = (DEBUG_SLOT + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

CURRENT_SLOT = (-1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

SLOT = enum_anon_21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 967

enum_anon_22 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

NO_BUTTON = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

UP_BUTTON = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

ENTER_BUTTON = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

DOWN_BUTTON = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

RIGHT_BUTTON = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

LEFT_BUTTON = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

BACK_BUTTON = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

ANY_BUTTON = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

BUTTONTYPES = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

BUTTONTYPE = enum_anon_22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 989

enum_anon_23 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

EXP = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MOD = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

FLOOR = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

CEIL = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

ROUND = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

ABS = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

NEGATE = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

SQRT = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

LOG = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

LN = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

SIN = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

COS = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

TAN = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

ASIN = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

ACOS = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

ATAN = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MOD8 = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MOD16 = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MOD32 = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

POW = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

TRUNC = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MATHTYPES = (TRUNC + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

MATHTYPE = enum_anon_23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1024

enum_anon_24 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_OPEN = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_CLOSE = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_READ_PINS = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_WRITE_PINS = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_READ_ADC = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_WRITE_UART = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_READ_UART = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_ENABLE_UART = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_DISABLE_UART = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_ACCU_SWITCH = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_BOOT_MODE2 = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_POLL_MODE2 = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_CLOSE_MODE2 = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_RAM_CHECK = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_SUBCODES = (TST_RAM_CHECK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

TST_SUBCODE = enum_anon_24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1053

enum_anon_25 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSE_FOLDERS = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSE_FOLDS_FILES = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSE_CACHE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSE_FILES = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSERTYPES = (BROWSE_FILES + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

BROWSERTYPE = enum_anon_25 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1071

enum_anon_26 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

NORMAL_FONT = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

SMALL_FONT = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

LARGE_FONT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

TINY_FONT = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

FONTTYPES = (TINY_FONT + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

FONTTYPE = enum_anon_26 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1089

enum_anon_27 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

NORMAL_ICON = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

SMALL_ICON = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

LARGE_ICON = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

MENU_ICON = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

ARROW_ICON = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

ICONTYPES = (ARROW_ICON + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

ICONTYPE = enum_anon_27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1108

enum_anon_28 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_CHARGING = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BATT_4 = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BATT_3 = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BATT_2 = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BATT_1 = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BATT_0 = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WAIT1 = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WAIT2 = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BT_ON = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BT_VISIBLE = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BT_CONNECTED = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_BT_CONNVISIB = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WIFI_3 = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WIFI_2 = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WIFI_1 = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_WIFI_CONNECTED = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

SICON_USB = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

S_ICON_NOS = (SICON_USB + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

S_ICON_NO = enum_anon_28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1134

enum_anon_29 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_NONE = (-1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_RUN = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_FOLDER = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_FOLDER2 = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_USB = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_SD = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_SOUND = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_IMAGE = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_SETTINGS = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_ONOFF = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_SEARCH = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_WIFI = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_CONNECTIONS = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_ADD_HIDDEN = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_TRASHBIN = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_VISIBILITY = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_KEY = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_CONNECT = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_DISCONNECT = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_UP = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_DOWN = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_WAIT1 = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_WAIT2 = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_BLUETOOTH = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_INFO = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_TEXT = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_QUESTIONMARK = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_INFO_FILE = 28 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_DISC = 29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_CONNECTED = 30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_OBP = 31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_OBD = 32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_OPENFOLDER = 33 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

ICON_BRICK1 = 34 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

N_ICON_NOS = (ICON_BRICK1 + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

N_ICON_NO = enum_anon_29 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1177

enum_anon_30 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

YES_NOTSEL = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

YES_SEL = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

NO_NOTSEL = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

NO_SEL = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

OFF = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WAIT_VERT = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WAIT_HORZ = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_MANUAL = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WARNSIGN = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WARN_BATT = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WARN_POWER = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WARN_TEMP = 11 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

NO_USBSTICK = 12 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_EXECUTE = 13 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_BRICK = 14 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_SDCARD = 15 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_USBSTICK = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_BLUETOOTH = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_WIFI = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_TRASH = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_COPY = 20 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

TO_FILE = 21 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

CHAR_ERROR = 22 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

COPY_ERROR = 23 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

PROGRAM_ERROR = 24 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

WARN_MEMORY = 27 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

L_ICON_NOS = (WARN_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

L_ICON_NO = enum_anon_30 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1212

enum_anon_31 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_STAR = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_LOCKSTAR = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_LOCK = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_PC = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_PHONE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_BRICK = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_UNKNOWN = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_FROM_FOLDER = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_CHECKBOX = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_CHECKED = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

ICON_XED = 10 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

M_ICON_NOS = (ICON_XED + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

M_ICON_NO = enum_anon_31 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1231

enum_anon_32 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1242

ICON_LEFT = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1242

ICON_RIGHT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1242

A_ICON_NOS = (ICON_RIGHT + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1242

A_ICON_NO = enum_anon_32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1242

enum_anon_33 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPE_PC = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPE_PHONE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPE_BRICK = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPE_UNKNOWN = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPES = (BTTYPE_UNKNOWN + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

BTTYPE = enum_anon_33 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1261

enum_anon_34 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_BLACK = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_GREEN = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_RED = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_ORANGE = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_GREEN_FLASH = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_RED_FLASH = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_ORANGE_FLASH = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_GREEN_PULSE = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_RED_PULSE = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LED_ORANGE_PULSE = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LEDPATTERNS = (LED_ORANGE_PULSE + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

LEDPATTERN = enum_anon_34 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1286

enum_anon_35 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LED_ALL = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LED_RR = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LED_RG = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LED_LR = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LED_LG = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

LEDTYPE = enum_anon_35 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1300

enum_anon_36 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

FILETYPE_UNKNOWN = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_FOLDER = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_SOUND = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_BYTECODE = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_GRAPHICS = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_DATALOG = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_PROGRAM = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_TEXT = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_SDCARD = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_USBSTICK = 32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

FILETYPES = (TYPE_USBSTICK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_RESTART_BROWSER = (-1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

TYPE_REFRESH_BROWSER = (-2) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

FILETYPE = enum_anon_36 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1326

enum_anon_37 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

OK = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

BUSY = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

FAIL = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

STOP = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

RESULT = enum_anon_37 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1345

enum_anon_38 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_8 = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_16 = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_32 = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_F = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_S = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_A = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_V = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_PCT = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_RAW = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_SI = 19 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_FORMATS = (DATA_SI + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

DATA_FORMAT = enum_anon_38 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1373

enum_anon_39 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_NONE = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_TAB = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_SPACE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_RETURN = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_COLON = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_COMMA = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_LINEFEED = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL_CRLF = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DELS = (DEL_CRLF + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

DEL = enum_anon_39 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1400

enum_anon_40 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

HW_USB = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

HW_BT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

HW_WIFI = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

HWTYPES = (HW_WIFI + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

HWTYPE = enum_anon_40 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1420

enum_anon_41 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1436

ENCRYPT_NONE = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1436

ENCRYPT_WPA2 = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1436

ENCRYPTS = (ENCRYPT_WPA2 + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1436

ENCRYPT = enum_anon_41 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1436

enum_anon_42 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1448

MODE_KEEP = (-1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1448

TYPE_KEEP = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1448

MIXS = (TYPE_KEEP + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1448

MIX = enum_anon_42 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1448

enum_anon_43 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

RED = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

GREEN = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

BLUE = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

BLANK = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

COLORS = (BLANK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

COLOR = enum_anon_43 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1459

enum_anon_44 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

BLACKCOLOR = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

BLUECOLOR = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

GREENCOLOR = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

YELLOWCOLOR = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

REDCOLOR = 5 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

WHITECOLOR = 6 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

NXTCOLOR = enum_anon_44 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1473

enum_anon_45 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_TEMP = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_CURRENT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_VOLTAGE = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_MEMORY = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_DSPSTAT = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_BATTLOW = 64 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING_BUSY = 128 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNINGS = 63 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

WARNING = enum_anon_45 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1489

enum_anon_46 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

RUNNING = 16 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

WAITING = 32 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

STOPPED = 64 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

HALTED = 128 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

OBJSTAT = enum_anon_46 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1520

enum_anon_47 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

DEVCMD_RESET = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

DEVCMD_FIRE = 17 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

DEVCMD_CHANNEL = 18 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

DEVCMDS = (DEVCMD_CHANNEL + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

DEVCMD = enum_anon_47 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1537

__u_char = c_ubyte # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 31

__u_short = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 32

__u_int = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 33

__u_long = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 34

__int8_t = c_char # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 37

__uint8_t = c_ubyte # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 38

__int16_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 39

__uint16_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 40

__int32_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 41

__uint32_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 42

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 62
class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    '__val',
]
struct_anon_48._fields_ = [
    ('__val', c_long * 2),
]

__quad_t = struct_anon_48 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 62

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 66
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    '__val',
]
struct_anon_49._fields_ = [
    ('__val', __u_long * 2),
]

__u_quad_t = struct_anon_49 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 66

__dev_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 134

__uid_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 135

__gid_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 136

__ino_t = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 137

__ino64_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 138

__mode_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 139

__nlink_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 140

__off_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 141

__off64_t = __quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 142

__pid_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 143

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 144
class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    '__val',
]
struct_anon_50._fields_ = [
    ('__val', c_int * 2),
]

__fsid_t = struct_anon_50 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 144

__clock_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 145

__rlim_t = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 146

__rlim64_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 147

__id_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 148

__time_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 149

__useconds_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 150

__suseconds_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 151

__daddr_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 153

__swblk_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 154

__key_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 155

__clockid_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 158

__timer_t = POINTER(None) # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 161

__blksize_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 164

__blkcnt_t = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 169

__blkcnt64_t = __quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 170

__fsblkcnt_t = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 173

__fsblkcnt64_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 174

__fsfilcnt_t = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 177

__fsfilcnt64_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 178

__ssize_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 180

__loff_t = __off64_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 184

__qaddr_t = POINTER(__quad_t) # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 185

__caddr_t = String # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 186

__intptr_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 189

__socklen_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 192

u_char = __u_char # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 35

u_short = __u_short # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 36

u_int = __u_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 37

u_long = __u_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 38

quad_t = __quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 39

u_quad_t = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 40

fsid_t = __fsid_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 41

loff_t = __loff_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 46

ino_t = __ino_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 50

dev_t = __dev_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 62

gid_t = __gid_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 67

mode_t = __mode_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 72

nlink_t = __nlink_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 77

uid_t = __uid_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 82

off_t = __off_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 88

pid_t = __pid_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 100

id_t = __id_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 105

ssize_t = __ssize_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 110

daddr_t = __daddr_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 116

caddr_t = __caddr_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 117

key_t = __key_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 123

time_t = __time_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 77

clockid_t = __clockid_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 93

timer_t = __timer_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 105

ulong = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 151

ushort = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 152

uint = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 153

int8_t = c_char # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 163

int16_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 164

int32_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 165

u_int8_t = c_ubyte # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 174

u_int16_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 175

u_int32_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 176

register_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 183

__sig_atomic_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/sigset.h: 24

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/sigset.h: 32
class struct_anon_51(Structure):
    pass

struct_anon_51.__slots__ = [
    '__val',
]
struct_anon_51._fields_ = [
    ('__val', c_ulong * (1024 / (8 * sizeof(c_ulong)))),
]

__sigset_t = struct_anon_51 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/sigset.h: 32

sigset_t = __sigset_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 38

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 121
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/time.h: 69
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

suseconds_t = __suseconds_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 49

__fd_mask = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 55

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 78
class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    '__fds_bits',
]
struct_anon_52._fields_ = [
    ('__fds_bits', __fd_mask * (1024 / (8 * sizeof(__fd_mask)))),
]

fd_set = struct_anon_52 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 78

fd_mask = __fd_mask # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 85

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 109
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'select'):
        continue
    select = _lib.select
    select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timeval)]
    select.restype = c_int
    break

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 121
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'pselect'):
        continue
    pselect = _lib.pselect
    pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timespec), POINTER(__sigset_t)]
    pselect.restype = c_int
    break

blkcnt_t = __blkcnt_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 235

fsblkcnt_t = __fsblkcnt_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 239

fsfilcnt_t = __fsfilcnt_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 243

pthread_t = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 38

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 45
class union_anon_53(Union):
    pass

union_anon_53.__slots__ = [
    '__size',
    '__align',
]
union_anon_53._fields_ = [
    ('__size', c_char * 36),
    ('__align', c_long),
]

pthread_attr_t = union_anon_53 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 45

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 48
class struct___pthread_internal_slist(Structure):
    pass

struct___pthread_internal_slist.__slots__ = [
    '__next',
]
struct___pthread_internal_slist._fields_ = [
    ('__next', POINTER(struct___pthread_internal_slist)),
]

__pthread_slist_t = struct___pthread_internal_slist # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 51

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 67
class union_anon_54(Union):
    pass

union_anon_54.__slots__ = [
    '__spins',
    '__list',
]
union_anon_54._fields_ = [
    ('__spins', c_int),
    ('__list', __pthread_slist_t),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 58
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__kind',
    '__nusers',
    'unnamed_1',
]
struct___pthread_mutex_s._anonymous_ = [
    'unnamed_1',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__kind', c_int),
    ('__nusers', c_uint),
    ('unnamed_1', union_anon_54),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 75
class union_anon_55(Union):
    pass

union_anon_55.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_55._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * 24),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_55 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 75

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 81
class union_anon_56(Union):
    pass

union_anon_56.__slots__ = [
    '__size',
    '__align',
]
union_anon_56._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_long),
]

pthread_mutexattr_t = union_anon_56 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 81

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 88
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    '__lock',
    '__futex',
    '__total_seq',
    '__wakeup_seq',
    '__woken_seq',
    '__mutex',
    '__nwaiters',
    '__broadcast_seq',
]
struct_anon_57._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', POINTER(None)),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 101
class union_anon_58(Union):
    pass

union_anon_58.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_58._fields_ = [
    ('__data', struct_anon_57),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_58 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 101

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 107
class union_anon_59(Union):
    pass

union_anon_59.__slots__ = [
    '__size',
    '__align',
]
union_anon_59._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_long),
]

pthread_condattr_t = union_anon_59 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 107

pthread_key_t = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 111

pthread_once_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 115

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 123
class struct_anon_60(Structure):
    pass

struct_anon_60.__slots__ = [
    '__lock',
    '__nr_readers',
    '__readers_wakeup',
    '__writer_wakeup',
    '__nr_readers_queued',
    '__nr_writers_queued',
    '__flags',
    '__shared',
    '__pad1',
    '__pad2',
    '__writer',
]
struct_anon_60._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__flags', c_ubyte),
    ('__shared', c_ubyte),
    ('__pad1', c_ubyte),
    ('__pad2', c_ubyte),
    ('__writer', c_int),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 150
class union_anon_61(Union):
    pass

union_anon_61.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_61._fields_ = [
    ('__data', struct_anon_60),
    ('__size', c_char * 32),
    ('__align', c_long),
]

pthread_rwlock_t = union_anon_61 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 150

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 156
class union_anon_62(Union):
    pass

union_anon_62.__slots__ = [
    '__size',
    '__align',
]
union_anon_62._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]

pthread_rwlockattr_t = union_anon_62 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 156

pthread_spinlock_t = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 162

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 171
class union_anon_63(Union):
    pass

union_anon_63.__slots__ = [
    '__size',
    '__align',
]
union_anon_63._fields_ = [
    ('__size', c_char * 20),
    ('__align', c_long),
]

pthread_barrier_t = union_anon_63 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 171

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 177
class union_anon_64(Union):
    pass

union_anon_64.__slots__ = [
    '__size',
    '__align',
]
union_anon_64._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]

pthread_barrierattr_t = union_anon_64 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 177

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 28
class struct_winsize(Structure):
    pass

struct_winsize.__slots__ = [
    'ws_row',
    'ws_col',
    'ws_xpixel',
    'ws_ypixel',
]
struct_winsize._fields_ = [
    ('ws_row', c_uint),
    ('ws_col', c_uint),
    ('ws_xpixel', c_uint),
    ('ws_ypixel', c_uint),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 37
class struct_termio(Structure):
    pass

struct_termio.__slots__ = [
    'c_iflag',
    'c_oflag',
    'c_cflag',
    'c_lflag',
    'c_line',
    'c_cc',
]
struct_termio._fields_ = [
    ('c_iflag', c_uint),
    ('c_oflag', c_uint),
    ('c_cflag', c_uint),
    ('c_lflag', c_uint),
    ('c_line', c_ubyte),
    ('c_cc', c_ubyte * 8),
]

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ioctl.h: 42
for _lib in _libs.values():
    if hasattr(_lib, 'ioctl'):
        _func = _lib.ioctl
        _restype = c_int
        _argtypes = [c_int, c_ulong]
        ioctl = _variadic_function(_func,_restype,_argtypes)

enum_anon_65 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 556

FALSE = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 556

TRUE = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 556

enum_anon_66 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_TOUCH = 1 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_LIGHT = 2 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_SOUND = 3 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_COLOR = 4 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_TACHO = 7 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_MINITACHO = 8 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NEWTACHO = 9 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_THIRD_PARTY_START = 50 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_THIRD_PARTY_END = 99 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_IIC_UNKNOWN = 100 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_TEST = 101 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NXT_IIC = 123 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_TERMINAL = 124 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_UNKNOWN = 125 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_NONE = 126 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE_ERROR = 127 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

TYPE = enum_anon_66 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 589

enum_anon_67 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_UNKNOWN = 111 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_DAISYCHAIN = 117 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_NXT_COLOR = 118 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_NXT_DUMB = 119 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_NXT_IIC = 120 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_INPUT_DUMB = 121 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_INPUT_UART = 122 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_OUTPUT_DUMB = 123 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_OUTPUT_INTELLIGENT = 124 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_OUTPUT_TACHO = 125 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_NONE = 126 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN_ERROR = 127 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

CONN = enum_anon_67 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 623

enum_anon_68 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

NOBREAK = 256 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

STOPBREAK = 512 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

SLEEPBREAK = 1024 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

INSTRBREAK = 2048 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

BUSYBREAK = 4096 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

PRGBREAK = 8192 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

USERBREAK = 16384 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

FAILBREAK = 32768 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

DSPSTAT = enum_anon_68 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 677

PRIM = CFUNCTYPE(UNCHECKED(None), ) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 679

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 712
class union_anon_69(Union):
    pass

union_anon_69.__slots__ = [
    'CallerId',
    'TriggerCount',
]
union_anon_69._fields_ = [
    ('CallerId', OBJID),
    ('TriggerCount', TRIGGER),
]

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 719
class struct_anon_70(Structure):
    pass

struct_anon_70.__slots__ = [
    'Ip',
    'pLocal',
    'ObjStatus',
    'Blocked',
    'u',
    'Local',
]
struct_anon_70._fields_ = [
    ('Ip', IP),
    ('pLocal', LP),
    ('ObjStatus', UBYTE),
    ('Blocked', UBYTE),
    ('u', union_anon_69),
    ('Local', POINTER(VARDATA)),
]

OBJ = struct_anon_70 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 719

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 730
class struct_anon_71(Structure):
    pass

struct_anon_71.__slots__ = [
    'Addr',
    'OpCode',
]
struct_anon_71._fields_ = [
    ('Addr', IMINDEX),
    ('OpCode', OP),
]

BRKP = struct_anon_71 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 730

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 766
class struct_anon_72(Structure):
    pass

struct_anon_72.__slots__ = [
    'InstrCnt',
    'InstrTime',
    'StartTime',
    'RunTime',
    'pImage',
    'pData',
    'pGlobal',
    'pObjHead',
    'pObjList',
    'ObjectIp',
    'ObjectLocal',
    'Objects',
    'ObjectId',
    'Status',
    'StatusChange',
    'Result',
    'Brkp',
    'Label',
    'Debug',
    'Name',
]
struct_anon_72._fields_ = [
    ('InstrCnt', ULONG),
    ('InstrTime', ULONG),
    ('StartTime', ULONG),
    ('RunTime', ULONG),
    ('pImage', IP),
    ('pData', GP),
    ('pGlobal', GP),
    ('pObjHead', POINTER(OBJHEAD)),
    ('pObjList', POINTER(POINTER(OBJ))),
    ('ObjectIp', IP),
    ('ObjectLocal', LP),
    ('Objects', OBJID),
    ('ObjectId', OBJID),
    ('Status', OBJSTAT),
    ('StatusChange', OBJSTAT),
    ('Result', RESULT),
    ('Brkp', BRKP * 4),
    ('Label', LABEL * 32),
    ('Debug', UWORD),
    ('Name', DATA8 * 52),
]

PRG = struct_anon_72 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 766

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 798
class struct_anon_73(Structure):
    pass

struct_anon_73.__slots__ = [
    'Name',
    'Type',
    'Connection',
    'Mode',
    'DataSets',
    'Format',
    'Figures',
    'Decimals',
    'Views',
    'RawMin',
    'RawMax',
    'PctMin',
    'PctMax',
    'SiMin',
    'SiMax',
    'InvalidTime',
    'IdValue',
    'Pins',
    'Symbol',
    'Align',
]
struct_anon_73._fields_ = [
    ('Name', SBYTE * (11 + 1)),
    ('Type', DATA8),
    ('Connection', DATA8),
    ('Mode', DATA8),
    ('DataSets', DATA8),
    ('Format', DATA8),
    ('Figures', DATA8),
    ('Decimals', DATA8),
    ('Views', DATA8),
    ('RawMin', DATAF),
    ('RawMax', DATAF),
    ('PctMin', DATAF),
    ('PctMax', DATAF),
    ('SiMin', DATAF),
    ('SiMax', DATAF),
    ('InvalidTime', UWORD),
    ('IdValue', UWORD),
    ('Pins', DATA8),
    ('Symbol', SBYTE * (4 + 1)),
    ('Align', UWORD),
]

TYPES = struct_anon_73 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 798

enum_anon_74 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

TOO_MANY_ERRORS_TO_BUFFER = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

TYPEDATA_TABEL_FULL = (TOO_MANY_ERRORS_TO_BUFFER + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

TYPEDATA_FILE_NOT_FOUND = (TYPEDATA_TABEL_FULL + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

ANALOG_DEVICE_FILE_NOT_FOUND = (TYPEDATA_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

ANALOG_SHARED_MEMORY = (ANALOG_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

UART_DEVICE_FILE_NOT_FOUND = (ANALOG_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

UART_SHARED_MEMORY = (UART_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

IIC_DEVICE_FILE_NOT_FOUND = (UART_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

IIC_SHARED_MEMORY = (IIC_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

DISPLAY_SHARED_MEMORY = (IIC_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

UI_SHARED_MEMORY = (DISPLAY_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

UI_DEVICE_FILE_NOT_FOUND = (UI_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

LCD_DEVICE_FILE_NOT_FOUND = (UI_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

OUTPUT_SHARED_MEMORY = (LCD_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

COM_COULD_NOT_OPEN_FILE = (OUTPUT_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

COM_NAME_TOO_SHORT = (COM_COULD_NOT_OPEN_FILE + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

COM_NAME_TOO_LONG = (COM_NAME_TOO_SHORT + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

COM_INTERNAL = (COM_NAME_TOO_LONG + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_INTERNAL = (COM_INTERNAL + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_PROGRAM_VALIDATION = (VM_INTERNAL + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_PROGRAM_NOT_STARTED = (VM_PROGRAM_VALIDATION + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_PROGRAM_FAIL_BREAK = (VM_PROGRAM_NOT_STARTED + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_PROGRAM_INSTRUCTION_BREAK = (VM_PROGRAM_FAIL_BREAK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

VM_PROGRAM_NOT_FOUND = (VM_PROGRAM_INSTRUCTION_BREAK + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

SOUND_DEVICE_FILE_NOT_FOUND = (VM_PROGRAM_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

SOUND_SHARED_MEMORY = (SOUND_DEVICE_FILE_NOT_FOUND + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_OPEN_ERROR = (SOUND_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_READ_ERROR = (FILE_OPEN_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_WRITE_ERROR = (FILE_READ_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_CLOSE_ERROR = (FILE_WRITE_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_GET_HANDLE_ERROR = (FILE_CLOSE_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

FILE_NAME_ERROR = (FILE_GET_HANDLE_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

USB_SHARED_MEMORY = (FILE_NAME_ERROR + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

OUT_OF_MEMORY = (USB_SHARED_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

ERRORS = (OUT_OF_MEMORY + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

ERR = enum_anon_74 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 846

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 850
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'PrimParAdvance'):
        continue
    PrimParAdvance = _lib.PrimParAdvance
    PrimParAdvance.argtypes = []
    PrimParAdvance.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 852
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'PrimParPointer'):
        continue
    PrimParPointer = _lib.PrimParPointer
    PrimParPointer.argtypes = []
    PrimParPointer.restype = POINTER(None)
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 854
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetImageStart'):
        continue
    GetImageStart = _lib.GetImageStart
    GetImageStart.argtypes = []
    GetImageStart.restype = IP
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 856
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetDispatchStatus'):
        continue
    SetDispatchStatus = _lib.SetDispatchStatus
    SetDispatchStatus.argtypes = [DSPSTAT]
    SetDispatchStatus.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 858
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetInstructions'):
        continue
    SetInstructions = _lib.SetInstructions
    SetInstructions.argtypes = [ULONG]
    SetInstructions.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 860
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'CurrentProgramId'):
        continue
    CurrentProgramId = _lib.CurrentProgramId
    CurrentProgramId.argtypes = []
    CurrentProgramId.restype = PRGID
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 862
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ProgramStatus'):
        continue
    ProgramStatus = _lib.ProgramStatus
    ProgramStatus.argtypes = [PRGID]
    ProgramStatus.restype = OBJSTAT
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 864
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ProgramStatusChange'):
        continue
    ProgramStatusChange = _lib.ProgramStatusChange
    ProgramStatusChange.argtypes = [PRGID]
    ProgramStatusChange.restype = OBJSTAT
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 866
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ProgramEnd'):
        continue
    ProgramEnd = _lib.ProgramEnd
    ProgramEnd.argtypes = [PRGID]
    ProgramEnd.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 868
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'CallingObjectId'):
        continue
    CallingObjectId = _lib.CallingObjectId
    CallingObjectId.argtypes = []
    CallingObjectId.restype = OBJID
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 870
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'AdjustObjectIp'):
        continue
    AdjustObjectIp = _lib.AdjustObjectIp
    AdjustObjectIp.argtypes = [IMOFFS]
    AdjustObjectIp.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 872
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetObjectIp'):
        continue
    GetObjectIp = _lib.GetObjectIp
    GetObjectIp.argtypes = []
    GetObjectIp.restype = IP
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 874
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetObjectIp'):
        continue
    SetObjectIp = _lib.SetObjectIp
    SetObjectIp.argtypes = [IP]
    SetObjectIp.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 876
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetTimeUS'):
        continue
    GetTimeUS = _lib.GetTimeUS
    GetTimeUS.argtypes = []
    GetTimeUS.restype = ULONG
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 878
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetTimeMS'):
        continue
    GetTimeMS = _lib.GetTimeMS
    GetTimeMS.argtypes = []
    GetTimeMS.restype = ULONG
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 880
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetTime'):
        continue
    GetTime = _lib.GetTime
    GetTime.argtypes = []
    GetTime.restype = ULONG
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 882
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'CurrentObjectIp'):
        continue
    CurrentObjectIp = _lib.CurrentObjectIp
    CurrentObjectIp.argtypes = []
    CurrentObjectIp.restype = ULONG
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 884
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'VmPrint'):
        continue
    VmPrint = _lib.VmPrint
    VmPrint.argtypes = [String]
    VmPrint.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 886
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetTerminalEnable'):
        continue
    SetTerminalEnable = _lib.SetTerminalEnable
    SetTerminalEnable.argtypes = [DATA8]
    SetTerminalEnable.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 888
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetTerminalEnable'):
        continue
    GetTerminalEnable = _lib.GetTerminalEnable
    GetTerminalEnable.argtypes = []
    GetTerminalEnable.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 890
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetResourcePath'):
        continue
    GetResourcePath = _lib.GetResourcePath
    GetResourcePath.argtypes = [String, DATA8]
    GetResourcePath.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 892
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'VmMemoryResize'):
        continue
    VmMemoryResize = _lib.VmMemoryResize
    VmMemoryResize.argtypes = [HANDLER, DATA32]
    VmMemoryResize.restype = POINTER(None)
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 894
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetVolumePercent'):
        continue
    SetVolumePercent = _lib.SetVolumePercent
    SetVolumePercent.argtypes = [DATA8]
    SetVolumePercent.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 896
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetVolumePercent'):
        continue
    GetVolumePercent = _lib.GetVolumePercent
    GetVolumePercent.argtypes = []
    GetVolumePercent.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 898
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetSleepMinutes'):
        continue
    SetSleepMinutes = _lib.SetSleepMinutes
    SetSleepMinutes.argtypes = [DATA8]
    SetSleepMinutes.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 900
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GetSleepMinutes'):
        continue
    GetSleepMinutes = _lib.GetSleepMinutes
    GetSleepMinutes.argtypes = []
    GetSleepMinutes.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 902
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ExecuteByteCode'):
        continue
    ExecuteByteCode = _lib.ExecuteByteCode
    ExecuteByteCode.argtypes = [IP, GP, LP]
    ExecuteByteCode.restype = DSPSTAT
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 904
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'CheckSdcard'):
        continue
    CheckSdcard = _lib.CheckSdcard
    CheckSdcard.argtypes = [POINTER(DATA8), POINTER(DATA32), POINTER(DATA32), DATA8]
    CheckSdcard.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 906
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'CheckUsbstick'):
        continue
    CheckUsbstick = _lib.CheckUsbstick
    CheckUsbstick.argtypes = [POINTER(DATA8), POINTER(DATA32), POINTER(DATA32), DATA8]
    CheckUsbstick.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 908
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SetUiUpdate'):
        continue
    SetUiUpdate = _lib.SetUiUpdate
    SetUiUpdate.argtypes = []
    SetUiUpdate.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 910
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ValidateChar'):
        continue
    ValidateChar = _lib.ValidateChar
    ValidateChar.argtypes = [POINTER(DATA8), DATA8]
    ValidateChar.restype = RESULT
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 912
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ValidateString'):
        continue
    ValidateString = _lib.ValidateString
    ValidateString.argtypes = [POINTER(DATA8), DATA8]
    ValidateString.restype = RESULT
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 914
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LogErrorGet'):
        continue
    LogErrorGet = _lib.LogErrorGet
    LogErrorGet.argtypes = []
    LogErrorGet.restype = ERR
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 924
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LogErrorNumber'):
        continue
    LogErrorNumber = _lib.LogErrorNumber
    LogErrorNumber.argtypes = [ERR]
    LogErrorNumber.restype = None
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 925
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LogErrorNumberExists'):
        continue
    LogErrorNumberExists = _lib.LogErrorNumberExists
    LogErrorNumberExists.argtypes = [ERR]
    LogErrorNumberExists.restype = DATA8
    break

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 952
class struct_anon_75(Structure):
    pass

struct_anon_75.__slots__ = [
    'Calibration',
    'CalLimits',
    'Crc',
    'ADRaw',
    'SensorRaw',
]
struct_anon_75._fields_ = [
    ('Calibration', (ULONG * 4) * 3),
    ('CalLimits', UWORD * (3 - 1)),
    ('Crc', UWORD),
    ('ADRaw', UWORD * 4),
    ('SensorRaw', UWORD * 4),
]

COLORSTRUCT = struct_anon_75 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 952

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1007
class struct_anon_76(Structure):
    pass

struct_anon_76.__slots__ = [
    'InPin1',
    'InPin6',
    'OutPin5',
    'BatteryTemp',
    'MotorCurrent',
    'BatteryCurrent',
    'Cell123456',
    'Pin1',
    'Pin6',
    'Actual',
    'LogIn',
    'LogOut',
    'NxtCol',
    'OutPin5Low',
    'Updated',
    'InDcm',
    'InConn',
    'OutDcm',
    'OutConn',
]
struct_anon_76._fields_ = [
    ('InPin1', DATA16 * 4),
    ('InPin6', DATA16 * 4),
    ('OutPin5', DATA16 * 4),
    ('BatteryTemp', DATA16),
    ('MotorCurrent', DATA16),
    ('BatteryCurrent', DATA16),
    ('Cell123456', DATA16),
    ('Pin1', (DATA16 * 300) * 4),
    ('Pin6', (DATA16 * 300) * 4),
    ('Actual', UWORD * 4),
    ('LogIn', UWORD * 4),
    ('LogOut', UWORD * 4),
    ('NxtCol', COLORSTRUCT * 4),
    ('OutPin5Low', DATA16 * 4),
    ('Updated', DATA8 * 4),
    ('InDcm', DATA8 * 4),
    ('InConn', DATA8 * 4),
    ('OutDcm', DATA8 * 4),
    ('OutConn', DATA8 * 4),
]

ANALOG = struct_anon_76 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1007

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1046
class struct_anon_77(Structure):
    pass

struct_anon_77.__slots__ = [
    'TypeData',
    'Repeat',
    'Raw',
    'Actual',
    'LogIn',
    'Status',
    'Output',
    'OutputLength',
]
struct_anon_77._fields_ = [
    ('TypeData', (TYPES * 8) * 4),
    ('Repeat', (UWORD * 300) * 4),
    ('Raw', ((DATA8 * 32) * 300) * 4),
    ('Actual', UWORD * 4),
    ('LogIn', UWORD * 4),
    ('Status', DATA8 * 4),
    ('Output', (DATA8 * 32) * 4),
    ('OutputLength', DATA8 * 4),
]

UART = struct_anon_77 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1046

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1065
class struct_anon_78(Structure):
    pass

struct_anon_78.__slots__ = [
    'Connection',
    'Type',
    'Mode',
]
struct_anon_78._fields_ = [
    ('Connection', DATA8 * 4),
    ('Type', DATA8 * 4),
    ('Mode', DATA8 * 4),
]

DEVCON = struct_anon_78 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1065

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1074
class struct_anon_79(Structure):
    pass

struct_anon_79.__slots__ = [
    'TypeData',
    'Port',
    'Mode',
]
struct_anon_79._fields_ = [
    ('TypeData', TYPES),
    ('Port', DATA8),
    ('Mode', DATA8),
]

UARTCTL = struct_anon_79 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1074

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1114
class struct_anon_80(Structure):
    pass

struct_anon_80.__slots__ = [
    'TypeData',
    'Repeat',
    'Raw',
    'Actual',
    'LogIn',
    'Status',
    'Changed',
    'Output',
    'OutputLength',
]
struct_anon_80._fields_ = [
    ('TypeData', (TYPES * 8) * 4),
    ('Repeat', (UWORD * 300) * 4),
    ('Raw', ((DATA8 * 32) * 300) * 4),
    ('Actual', UWORD * 4),
    ('LogIn', UWORD * 4),
    ('Status', DATA8 * 4),
    ('Changed', DATA8 * 4),
    ('Output', (DATA8 * 32) * 4),
    ('OutputLength', DATA8 * 4),
]

IIC = struct_anon_80 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1114

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1133
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    'TypeData',
    'Port',
    'Mode',
]
struct_anon_81._fields_ = [
    ('TypeData', TYPES),
    ('Port', DATA8),
    ('Mode', DATA8),
]

IICCTL = struct_anon_81 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1133

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1147
class struct_anon_82(Structure):
    pass

struct_anon_82.__slots__ = [
    'Result',
    'Port',
    'Repeat',
    'Time',
    'WrLng',
    'WrData',
    'RdLng',
    'RdData',
]
struct_anon_82._fields_ = [
    ('Result', RESULT),
    ('Port', DATA8),
    ('Repeat', DATA8),
    ('Time', DATA16),
    ('WrLng', DATA8),
    ('WrData', DATA8 * 32),
    ('RdLng', DATA8),
    ('RdData', DATA8 * 32),
]

IICDAT = struct_anon_82 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1147

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1164
class struct_anon_83(Structure):
    pass

struct_anon_83.__slots__ = [
    'Port',
    'Time',
    'Type',
    'Mode',
    'Manufacturer',
    'SensorType',
    'SetupLng',
    'SetupString',
    'PollLng',
    'PollString',
    'ReadLng',
]
struct_anon_83._fields_ = [
    ('Port', DATA8),
    ('Time', DATA16),
    ('Type', DATA8),
    ('Mode', DATA8),
    ('Manufacturer', DATA8 * (8 + 1)),
    ('SensorType', DATA8 * (8 + 1)),
    ('SetupLng', DATA8),
    ('SetupString', ULONG),
    ('PollLng', DATA8),
    ('PollString', ULONG),
    ('ReadLng', DATA8),
]

IICSTR = struct_anon_83 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1164

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1183
class struct_anon_84(Structure):
    pass

struct_anon_84.__slots__ = [
    'Port',
    'Length',
    'String',
]
struct_anon_84._fields_ = [
    ('Port', DATA8),
    ('Length', DATA8),
    ('String', DATA8 * (8 + 1)),
]

TSTPIN = struct_anon_84 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1183

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1202
class struct_anon_85(Structure):
    pass

struct_anon_85.__slots__ = [
    'Bitrate',
    'Port',
    'Length',
    'String',
]
struct_anon_85._fields_ = [
    ('Bitrate', DATA32),
    ('Port', DATA8),
    ('Length', DATA8),
    ('String', DATA8 * 64),
]

TSTUART = struct_anon_85 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1202

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1230
class struct_anon_86(Structure):
    pass

struct_anon_86.__slots__ = [
    'Pressed',
]
struct_anon_86._fields_ = [
    ('Pressed', DATA8 * 6),
]

UI = struct_anon_86 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1230

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1258
class struct_anon_87(Structure):
    pass

struct_anon_87.__slots__ = [
    'Lcd',
]
struct_anon_87._fields_ = [
    ('Lcd', UBYTE * (((178 + 7) / 8) * 128)),
]

LCD = struct_anon_87 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1258

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1282
class struct_anon_88(Structure):
    pass

struct_anon_88.__slots__ = [
    'Status',
]
struct_anon_88._fields_ = [
    ('Status', DATA8),
]

SOUND = struct_anon_88 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1282

enum_anon_89 = c_int # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1302

FULL_SPEED = 0 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1302

HIGH_SPEED = (FULL_SPEED + 1) # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1302

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1311
class struct_anon_90(Structure):
    pass

struct_anon_90.__slots__ = [
    'Speed',
]
struct_anon_90._fields_ = [
    ('Speed', DATA8),
]

USB_SPEED = struct_anon_90 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1311

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1334
class struct_anon_91(Structure):
    pass

struct_anon_91.__slots__ = [
    'VolumePercent',
    'SleepMinutes',
]
struct_anon_91._fields_ = [
    ('VolumePercent', DATA8),
    ('SleepMinutes', DATA8),
]

NONVOL = struct_anon_91 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1334

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1350
class struct_anon_92(Structure):
    pass

struct_anon_92.__slots__ = [
    'TachoCounts',
    'Speed',
    'TachoSensor',
]
struct_anon_92._fields_ = [
    ('TachoCounts', SLONG),
    ('Speed', SBYTE),
    ('TachoSensor', SLONG),
]

MOTORDATA = struct_anon_92 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1350

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1361
class struct_anon_93(Structure):
    pass

struct_anon_93.__slots__ = [
    'Cmd',
    'Nos',
    'Power',
    'Step1',
    'Step2',
    'Step3',
    'Brake',
]
struct_anon_93._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Power', DATA8),
    ('Step1', DATA32),
    ('Step2', DATA32),
    ('Step3', DATA32),
    ('Brake', DATA8),
]

STEPPOWER = struct_anon_93 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1361

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1372
class struct_anon_94(Structure):
    pass

struct_anon_94.__slots__ = [
    'Cmd',
    'Nos',
    'Power',
    'Time1',
    'Time2',
    'Time3',
    'Brake',
]
struct_anon_94._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Power', DATA8),
    ('Time1', DATA32),
    ('Time2', DATA32),
    ('Time3', DATA32),
    ('Brake', DATA8),
]

TIMEPOWER = struct_anon_94 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1372

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1383
class struct_anon_95(Structure):
    pass

struct_anon_95.__slots__ = [
    'Cmd',
    'Nos',
    'Speed',
    'Step1',
    'Step2',
    'Step3',
    'Brake',
]
struct_anon_95._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Speed', DATA8),
    ('Step1', DATA32),
    ('Step2', DATA32),
    ('Step3', DATA32),
    ('Brake', DATA8),
]

STEPSPEED = struct_anon_95 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1383

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1394
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'Cmd',
    'Nos',
    'Speed',
    'Time1',
    'Time2',
    'Time3',
    'Brake',
]
struct_anon_96._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Speed', DATA8),
    ('Time1', DATA32),
    ('Time2', DATA32),
    ('Time3', DATA32),
    ('Brake', DATA8),
]

TIMESPEED = struct_anon_96 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1394

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1404
class struct_anon_97(Structure):
    pass

struct_anon_97.__slots__ = [
    'Cmd',
    'Nos',
    'Speed',
    'Turn',
    'Step',
    'Brake',
]
struct_anon_97._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Speed', DATA8),
    ('Turn', DATA16),
    ('Step', DATA32),
    ('Brake', DATA8),
]

STEPSYNC = struct_anon_97 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1404

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1414
class struct_anon_98(Structure):
    pass

struct_anon_98.__slots__ = [
    'Cmd',
    'Nos',
    'Speed',
    'Turn',
    'Time',
    'Brake',
]
struct_anon_98._fields_ = [
    ('Cmd', DATA8),
    ('Nos', DATA8),
    ('Speed', DATA8),
    ('Turn', DATA16),
    ('Time', DATA32),
    ('Brake', DATA8),
]

TIMESYNC = struct_anon_98 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1414

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1513
class struct_anon_99(Structure):
    pass

struct_anon_99.__slots__ = [
    'NonVol',
    'FirstProgram',
    'PrintBuffer',
    'TerminalEnabled',
    'FavouritePrg',
    'ProgramId',
    'Program',
    'InstrCnt',
    'pImage',
    'pGlobal',
    'pObjHead',
    'pObjList',
    'ObjectIp',
    'ObjectLocal',
    'Objects',
    'ObjectId',
    'ObjIpSave',
    'ObjGlobalSave',
    'ObjLocalSave',
    'DispatchStatusSave',
    'PrioritySave',
    'TimerDataSec',
    'TimerDatanSec',
    'Debug',
    'Test',
    'RefCount',
    'TimeuS',
    'OldTime1',
    'OldTime2',
    'NewTime',
    'DispatchStatus',
    'Priority',
    'Value',
    'Handle',
    'Errors',
    'ErrorIn',
    'ErrorOut',
    'MemorySize',
    'MemoryFree',
    'MemoryTimer',
    'SdcardSize',
    'SdcardFree',
    'SdcardTimer',
    'SdcardOk',
    'LcdBuffer',
    'LcdUpdated',
    'Analog',
    'pAnalog',
    'AdcFile',
]
struct_anon_99._fields_ = [
    ('NonVol', NONVOL),
    ('FirstProgram', DATA8 * (((10 + 52) + 52) + 5)),
    ('PrintBuffer', c_char * (160 + 1)),
    ('TerminalEnabled', DATA8),
    ('FavouritePrg', PRGID),
    ('ProgramId', PRGID),
    ('Program', PRG * SLOTS),
    ('InstrCnt', ULONG),
    ('pImage', IP),
    ('pGlobal', GP),
    ('pObjHead', POINTER(OBJHEAD)),
    ('pObjList', POINTER(POINTER(OBJ))),
    ('ObjectIp', IP),
    ('ObjectLocal', LP),
    ('Objects', OBJID),
    ('ObjectId', OBJID),
    ('ObjIpSave', IP),
    ('ObjGlobalSave', GP),
    ('ObjLocalSave', LP),
    ('DispatchStatusSave', DSPSTAT),
    ('PrioritySave', ULONG),
    ('TimerDataSec', c_long),
    ('TimerDatanSec', c_long),
    ('Debug', UWORD),
    ('Test', UWORD),
    ('RefCount', UWORD),
    ('TimeuS', ULONG),
    ('OldTime1', ULONG),
    ('OldTime2', ULONG),
    ('NewTime', ULONG),
    ('DispatchStatus', DSPSTAT),
    ('Priority', ULONG),
    ('Value', ULONG),
    ('Handle', HANDLER),
    ('Errors', ERR * 8),
    ('ErrorIn', UBYTE),
    ('ErrorOut', UBYTE),
    ('MemorySize', DATA32),
    ('MemoryFree', DATA32),
    ('MemoryTimer', ULONG),
    ('SdcardSize', DATA32),
    ('SdcardFree', DATA32),
    ('SdcardTimer', ULONG),
    ('SdcardOk', DATA8),
    ('LcdBuffer', LCD),
    ('LcdUpdated', DATA8),
    ('Analog', ANALOG),
    ('pAnalog', POINTER(ANALOG)),
    ('AdcFile', c_int),
]

GLOBALS = struct_anon_99 # /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1513

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1526
for _lib in _libs.values():
    try:
        VMInstance = (GLOBALS).in_dll(_lib, 'VMInstance')
        break
    except:
        pass

__const = c_int # <command-line>: 4

# <command-line>: 7
try:
    CTYPESGEN = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 40
try:
    TERMINAL_ENABLED = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 41
try:
    DEBUG_UART = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 99
try:
    EP2 = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 100
try:
    FINALB = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 101
try:
    FINAL = 2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 102
try:
    SIMULATION = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 104
try:
    PLATFORM_START = FINAL
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 105
try:
    PLATFORM_END = EP2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 108
try:
    A4 = (-1)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 109
try:
    EVALBOARD = (-2)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 110
try:
    ONE2ONE = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 118
try:
    HARDWARE = FINAL
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 175
try:
    TESTDEVICE = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 25
try:
    BYTECODE_VERSION = 1.04
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 39
try:
    vmOUTPUTS = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 40
try:
    vmINPUTS = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 41
try:
    vmBUTTONS = 6
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 42
try:
    vmLEDS = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 44
try:
    vmLCD_WIDTH = 178
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 45
try:
    vmLCD_HEIGHT = 128
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 46
try:
    vmTOPLINE_HEIGHT = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 47
try:
    vmLCD_STORE_LEVELS = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 49
try:
    vmDEFAULT_VOLUME = 100
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 50
try:
    vmDEFAULT_SLEEPMINUTES = 30
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 54
try:
    vmFG_COLOR = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 55
try:
    vmBG_COLOR = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 57
try:
    vmCHAIN_DEPT = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 63
try:
    vmPATHSIZE = 84
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 64
try:
    vmNAMESIZE = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 65
try:
    vmEXTSIZE = 5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 66
try:
    vmFILENAMESIZE = 120
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 67
try:
    vmMACSIZE = 18
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 68
try:
    vmIPSIZE = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 69
try:
    vmBTADRSIZE = 13
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 71
try:
    vmERR_STRING_SIZE = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 73
try:
    vmEVENT_BT_PIN = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 74
try:
    vmEVENT_BT_REQ_CONF = 2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 76
try:
    vmMAX_VALID_TYPE = 101
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 80
try:
    vmMEMORY_FOLDER = '/mnt/ramdisk'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 81
try:
    vmPROGRAM_FOLDER = '../prjs/BrkProg_SAVE'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 82
try:
    vmDATALOG_FOLDER = '../prjs/BrkDL_SAVE'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 83
try:
    vmSDCARD_FOLDER = '../prjs/SD_Card'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 84
try:
    vmUSBSTICK_FOLDER = '../prjs/USB_Stick'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 86
try:
    vmPRJS_DIR = '../prjs'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 87
try:
    vmAPPS_DIR = '../apps'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 88
try:
    vmTOOLS_DIR = '../tools'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 89
try:
    vmTMP_DIR = '../tmp'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 91
try:
    vmSETTINGS_DIR = '../sys/settings'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 93
try:
    vmDIR_DEEPT = 127
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 97
try:
    vmLASTRUN_FILE_NAME = 'lastrun'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 98
try:
    vmCALDATA_FILE_NAME = 'caldata'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 102
try:
    vmSLEEP_FILE_NAME = 'Sleep'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 103
try:
    vmVOLUME_FILE_NAME = 'Volume'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 104
try:
    vmWIFI_FILE_NAME = 'WiFi'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 105
try:
    vmBLUETOOTH_FILE_NAME = 'Bluetooth'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 109
try:
    vmEXT_SOUND = '.rsf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 110
try:
    vmEXT_GRAPHICS = '.rgf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 111
try:
    vmEXT_BYTECODE = '.rbf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 112
try:
    vmEXT_TEXT = '.rtf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 113
try:
    vmEXT_DATALOG = '.rdf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 114
try:
    vmEXT_PROGRAM = '.rpf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 115
try:
    vmEXT_CONFIG = '.rcf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 116
try:
    vmEXT_ARCHIVE = '.raf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 120
try:
    vmBRICKNAMESIZE = 120
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 121
try:
    vmBTPASSKEYSIZE = 7
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 122
try:
    vmWIFIPASSKEYSIZE = 33
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 126
try:
    vmCHARSET_NAME = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 127
try:
    vmCHARSET_FILENAME = 2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 128
try:
    vmCHARSET_BTPASSKEY = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 129
try:
    vmCHARSET_WIFIPASSKEY = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 130
try:
    vmCHARSET_WIFISSID = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1492
try:
    DATA8_NAN = (-128)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1493
try:
    DATA16_NAN = (-32768)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1494
try:
    DATA32_NAN = 2147483648
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1495
try:
    DATAF_NAN = (0 / 0)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1497
try:
    DATA8_MIN = (-127)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1498
try:
    DATA8_MAX = 127
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1499
try:
    DATA16_MIN = (-32767)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1500
try:
    DATA16_MAX = 32767
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1501
try:
    DATA32_MIN = (-2147483647)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1502
try:
    DATA32_MAX = 2147483647
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1503
try:
    DATAF_MIN = (-2147483647)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1504
try:
    DATAF_MAX = 2147483647
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1547
try:
    vmPOP3_ABS_X = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1548
try:
    vmPOP3_ABS_Y = 50
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1550
try:
    vmPOP3_ABS_WARN_ICON_X = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1551
try:
    vmPOP3_ABS_WARN_ICON_X1 = 40
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1552
try:
    vmPOP3_ABS_WARN_ICON_X2 = 72
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1553
try:
    vmPOP3_ABS_WARN_ICON_X3 = 104
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1554
try:
    vmPOP3_ABS_WARN_ICON_Y = 60
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1555
try:
    vmPOP3_ABS_WARN_SPEC_ICON_X = 88
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1556
try:
    vmPOP3_ABS_WARN_SPEC_ICON_Y = 60
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1557
try:
    vmPOP3_ABS_WARN_TEXT_X = 80
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1558
try:
    vmPOP3_ABS_WARN_TEXT_Y = 68
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1559
try:
    vmPOP3_ABS_WARN_YES_X = 72
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1560
try:
    vmPOP3_ABS_WARN_YES_Y = 90
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1561
try:
    vmPOP3_ABS_WARN_LINE_X = 21
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1562
try:
    vmPOP3_ABS_WARN_LINE_Y = 89
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1563
try:
    vmPOP3_ABS_WARN_LINE_ENDX = 155
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1568
def BYTEToBytes(_x):
    return (_x & 255)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1584
try:
    PRIMPAR_SHORT = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1585
try:
    PRIMPAR_LONG = 128
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1587
try:
    PRIMPAR_CONST = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1588
try:
    PRIMPAR_VARIABEL = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1589
try:
    PRIMPAR_LOCAL = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1590
try:
    PRIMPAR_GLOBAL = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1591
try:
    PRIMPAR_HANDLE = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1592
try:
    PRIMPAR_ADDR = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1594
try:
    PRIMPAR_INDEX = 31
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1595
try:
    PRIMPAR_CONST_SIGN = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1596
try:
    PRIMPAR_VALUE = 63
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1598
try:
    PRIMPAR_BYTES = 7
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1600
try:
    PRIMPAR_STRING_OLD = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1601
try:
    PRIMPAR_1_BYTE = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1602
try:
    PRIMPAR_2_BYTES = 2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1603
try:
    PRIMPAR_4_BYTES = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1604
try:
    PRIMPAR_STRING = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1606
try:
    PRIMPAR_LABEL = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1608
def HND(x):
    return (PRIMPAR_HANDLE | x)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1609
def ADR(x):
    return (PRIMPAR_ADDR | x)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1611
try:
    LCS = (PRIMPAR_LONG | PRIMPAR_STRING)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1615
def LC0(v):
    return (((v & PRIMPAR_VALUE) | PRIMPAR_SHORT) | PRIMPAR_CONST)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1621
def LV0(i):
    return ((((i & PRIMPAR_INDEX) | PRIMPAR_SHORT) | PRIMPAR_VARIABEL) | PRIMPAR_LOCAL)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1627
def GV0(i):
    return ((((i & PRIMPAR_INDEX) | PRIMPAR_SHORT) | PRIMPAR_VARIABEL) | PRIMPAR_GLOBAL)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1636
try:
    CALLPAR_IN = 128
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1637
try:
    CALLPAR_OUT = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1639
try:
    CALLPAR_TYPE = 7
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1640
try:
    CALLPAR_DATA8 = DATA_8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1641
try:
    CALLPAR_DATA16 = DATA_16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1642
try:
    CALLPAR_DATA32 = DATA_32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1643
try:
    CALLPAR_DATAF = DATA_F
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1644
try:
    CALLPAR_STRING = DATA_S
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1646
try:
    IN_8 = (CALLPAR_IN | CALLPAR_DATA8)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1647
try:
    IN_16 = (CALLPAR_IN | CALLPAR_DATA16)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1648
try:
    IN_32 = (CALLPAR_IN | CALLPAR_DATA32)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1649
try:
    IN_F = (CALLPAR_IN | CALLPAR_DATAF)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1650
try:
    IN_S = (CALLPAR_IN | CALLPAR_STRING)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1651
try:
    OUT_8 = (CALLPAR_OUT | CALLPAR_DATA8)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1652
try:
    OUT_16 = (CALLPAR_OUT | CALLPAR_DATA16)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1653
try:
    OUT_32 = (CALLPAR_OUT | CALLPAR_DATA32)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1654
try:
    OUT_F = (CALLPAR_OUT | CALLPAR_DATAF)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1655
try:
    OUT_S = (CALLPAR_OUT | CALLPAR_STRING)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1657
try:
    IO_8 = (IN_8 | OUT_8)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1658
try:
    IO_16 = (IN_16 | OUT_16)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1659
try:
    IO_32 = (IN_32 | OUT_32)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1660
try:
    IO_F = (IN_F | OUT_F)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/bytecodes.h: 1661
try:
    IO_S = (IN_S | OUT_S)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 25
try:
    _SYS_TYPES_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 20
try:
    _FEATURES_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 123
try:
    __USE_ANSI = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 136
def __GNUC_PREREQ(maj, min):
    return 0

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 176
try:
    _BSD_SOURCE = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 177
try:
    _SVID_SOURCE = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 199
try:
    _POSIX_SOURCE = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 205
try:
    _POSIX_C_SOURCE = 200112L
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 210
try:
    __USE_POSIX = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 214
try:
    __USE_POSIX2 = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 218
try:
    __USE_POSIX199309 = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 222
try:
    __USE_POSIX199506 = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 226
try:
    __USE_XOPEN2K = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 261
try:
    __USE_MISC = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 265
try:
    __USE_BSD = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 269
try:
    __USE_SVID = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 292
try:
    __USE_FORTIFY_LEVEL = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 299
try:
    __STDC_ISO_10646__ = 200009L
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 308
try:
    __GNU_LIBRARY__ = 6
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 312
try:
    __GLIBC__ = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 313
try:
    __GLIBC_MINOR__ = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/features.h: 315
def __GLIBC_PREREQ(maj, min):
    return (((__GLIBC__ << 16) + __GLIBC_MINOR__) >= ((maj << 16) + min))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 21
try:
    _SYS_CDEFS_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 64
def __NTH(fct):
    return fct

__const = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 66

__signed = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 67

__volatile = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 68

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 74
def __P(args):
    return args

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 75
def __PMT(args):
    return args

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 81
def __STRING(x):
    return x

__ptr_t = POINTER(None) # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 84

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/wordsize.h: 19
try:
    __WORDSIZE = 32
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 370
def __LDBL_REDIR1(name, proto, alias):
    return (name + proto)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/cdefs.h: 371
def __LDBL_REDIR(name, proto):
    return (name + proto)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 25
try:
    _BITS_TYPES_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/wordsize.h: 19
try:
    __WORDSIZE = 32
except:
    pass

__S16_TYPE = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 99

__U16_TYPE = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 100

__S32_TYPE = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 101

__U32_TYPE = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 102

__SLONGWORD_TYPE = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 103

__ULONGWORD_TYPE = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 104

__SQUAD_TYPE = __quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 106

__UQUAD_TYPE = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 107

__SWORD_TYPE = c_int # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 108

__UWORD_TYPE = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 109

__SLONG32_TYPE = c_long # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 110

__ULONG32_TYPE = c_ulong # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 111

__S64_TYPE = __quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 112

__U64_TYPE = __u_quad_t # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/types.h: 113

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/typesizes.h: 25
try:
    _BITS_TYPESIZES_H = 1
except:
    pass

__TIMER_T_TYPE = POINTER(None) # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/typesizes.h: 57

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/typesizes.h: 59
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    '__val',
]
struct_anon_100._fields_ = [
    ('__val', c_int * 2),
]

__FSID_T_TYPE = struct_anon_100 # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/typesizes.h: 59

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/typesizes.h: 63
try:
    __FD_SETSIZE = 1024
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 71
try:
    __time_t_defined = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 88
try:
    __clockid_t_defined = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 100
try:
    __timer_t_defined = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/types.h: 212
try:
    __BIT_TYPES_DEFINED__ = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 20
try:
    _ENDIAN_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 32
try:
    __LITTLE_ENDIAN = 1234
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 33
try:
    __BIG_ENDIAN = 4321
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 34
try:
    __PDP_ENDIAN = 3412
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/endian.h: 9
try:
    __BYTE_ORDER = __LITTLE_ENDIAN
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/endian.h: 16
try:
    __FLOAT_WORD_ORDER = __BYTE_ORDER
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 46
try:
    LITTLE_ENDIAN = __LITTLE_ENDIAN
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 47
try:
    BIG_ENDIAN = __BIG_ENDIAN
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 48
try:
    PDP_ENDIAN = __PDP_ENDIAN
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/endian.h: 49
try:
    BYTE_ORDER = __BYTE_ORDER
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 23
try:
    _SYS_SELECT_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/select.h: 33
def __FD_SET(d, s):
    return (((__FDS_BITS (s)) [(__FDELT (d))]) | (__FDMASK (d)))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/select.h: 34
def __FD_CLR(d, s):
    return (((__FDS_BITS (s)) [(__FDELT (d))]) & (~((__FDMASK (d)).value)))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/select.h: 35
def __FD_ISSET(d, s):
    return (((((__FDS_BITS (s)).value) [((__FDELT (d)).value)]) & ((__FDMASK (d)).value)) != 0)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/sigset.h: 22
try:
    _SIGSET_H_types = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/sigset.h: 28
try:
    _SIGSET_NWORDS = (1024 / (8 * sizeof(c_ulong)))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 115
try:
    __timespec_defined = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/time.h: 64
try:
    _STRUCT_TIMEVAL = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 62
try:
    __NFDBITS = (8 * sizeof(__fd_mask))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 63
def __FDELT(d):
    return (d / __NFDBITS)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 64
def __FDMASK(d):
    return (1 << (d % __NFDBITS))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 76
def __FDS_BITS(set):
    return (set.contents.__fds_bits)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 81
try:
    FD_SETSIZE = __FD_SETSIZE
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 88
try:
    NFDBITS = __NFDBITS
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 93
def FD_SET(fd, fdsetp):
    return (__FD_SET (fd, fdsetp))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 94
def FD_CLR(fd, fdsetp):
    return (__FD_CLR (fd, fdsetp))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/select.h: 95
def FD_ISSET(fd, fdsetp):
    return (__FD_ISSET (fd, fdsetp))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/sysmacros.h: 22
try:
    _SYS_SYSMACROS_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 20
try:
    _BITS_PTHREADTYPES_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 24
try:
    __SIZEOF_PTHREAD_ATTR_T = 36
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 25
try:
    __SIZEOF_PTHREAD_MUTEX_T = 24
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 26
try:
    __SIZEOF_PTHREAD_MUTEXATTR_T = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 27
try:
    __SIZEOF_PTHREAD_COND_T = 48
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 28
try:
    __SIZEOF_PTHREAD_COND_COMPAT_T = 12
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 29
try:
    __SIZEOF_PTHREAD_CONDATTR_T = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 30
try:
    __SIZEOF_PTHREAD_RWLOCK_T = 32
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 31
try:
    __SIZEOF_PTHREAD_RWLOCKATTR_T = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 32
try:
    __SIZEOF_PTHREAD_BARRIER_T = 20
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 33
try:
    __SIZEOF_PTHREAD_BARRIERATTR_T = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ioctl.h: 20
try:
    _SYS_IOCTL_H = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 22
try:
    _IOC_NRBITS = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 23
try:
    _IOC_TYPEBITS = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 31
try:
    _IOC_SIZEBITS = 14
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 35
try:
    _IOC_DIRBITS = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 38
try:
    _IOC_NRMASK = ((1 << _IOC_NRBITS) - 1)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 39
try:
    _IOC_TYPEMASK = ((1 << _IOC_TYPEBITS) - 1)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 40
try:
    _IOC_SIZEMASK = ((1 << _IOC_SIZEBITS) - 1)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 41
try:
    _IOC_DIRMASK = ((1 << _IOC_DIRBITS) - 1)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 43
try:
    _IOC_NRSHIFT = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 44
try:
    _IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 45
try:
    _IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 46
try:
    _IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 54
try:
    _IOC_NONE = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 58
try:
    _IOC_WRITE = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 62
try:
    _IOC_READ = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 65
def _IOC(dir, type, nr, size):
    return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 71
def _IOC_TYPECHECK(t):
    return sizeof(t)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 74
def _IO(type, nr):
    return (_IOC (_IOC_NONE, type, nr, 0))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 75
def _IOR(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, (_IOC_TYPECHECK (size))))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 76
def _IOW(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, (_IOC_TYPECHECK (size))))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 77
def _IOWR(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, (_IOC_TYPECHECK (size))))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 78
def _IOR_BAD(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, sizeof(size)))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 79
def _IOW_BAD(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, sizeof(size)))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 80
def _IOWR_BAD(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, sizeof(size)))

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 83
def _IOC_DIR(nr):
    return ((nr >> _IOC_DIRSHIFT) & _IOC_DIRMASK)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 84
def _IOC_TYPE(nr):
    return ((nr >> _IOC_TYPESHIFT) & _IOC_TYPEMASK)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 85
def _IOC_NR(nr):
    return ((nr >> _IOC_NRSHIFT) & _IOC_NRMASK)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 86
def _IOC_SIZE(nr):
    return ((nr >> _IOC_SIZESHIFT) & _IOC_SIZEMASK)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 90
try:
    IOC_IN = (_IOC_WRITE << _IOC_DIRSHIFT)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 91
try:
    IOC_OUT = (_IOC_READ << _IOC_DIRSHIFT)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 92
try:
    IOC_INOUT = ((_IOC_WRITE | _IOC_READ) << _IOC_DIRSHIFT)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 93
try:
    IOCSIZE_MASK = (_IOC_SIZEMASK << _IOC_SIZESHIFT)
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/ioctl.h: 94
try:
    IOCSIZE_SHIFT = _IOC_SIZESHIFT
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 8
try:
    TCGETS = 21505
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 9
try:
    TCSETS = 21506
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 10
try:
    TCSETSW = 21507
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 11
try:
    TCSETSF = 21508
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 12
try:
    TCGETA = 21509
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 13
try:
    TCSETA = 21510
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 14
try:
    TCSETAW = 21511
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 15
try:
    TCSETAF = 21512
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 16
try:
    TCSBRK = 21513
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 17
try:
    TCXONC = 21514
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 18
try:
    TCFLSH = 21515
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 19
try:
    TIOCEXCL = 21516
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 20
try:
    TIOCNXCL = 21517
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 21
try:
    TIOCSCTTY = 21518
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 22
try:
    TIOCGPGRP = 21519
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 23
try:
    TIOCSPGRP = 21520
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 24
try:
    TIOCOUTQ = 21521
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 25
try:
    TIOCSTI = 21522
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 26
try:
    TIOCGWINSZ = 21523
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 27
try:
    TIOCSWINSZ = 21524
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 28
try:
    TIOCMGET = 21525
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 29
try:
    TIOCMBIS = 21526
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 30
try:
    TIOCMBIC = 21527
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 31
try:
    TIOCMSET = 21528
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 32
try:
    TIOCGSOFTCAR = 21529
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 33
try:
    TIOCSSOFTCAR = 21530
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 34
try:
    FIONREAD = 21531
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 35
try:
    TIOCINQ = FIONREAD
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 36
try:
    TIOCLINUX = 21532
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 37
try:
    TIOCCONS = 21533
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 38
try:
    TIOCGSERIAL = 21534
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 39
try:
    TIOCSSERIAL = 21535
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 40
try:
    TIOCPKT = 21536
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 41
try:
    FIONBIO = 21537
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 42
try:
    TIOCNOTTY = 21538
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 43
try:
    TIOCSETD = 21539
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 44
try:
    TIOCGETD = 21540
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 45
try:
    TCSBRKP = 21541
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 46
try:
    TIOCSBRK = 21543
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 47
try:
    TIOCCBRK = 21544
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 48
try:
    TIOCGSID = 21545
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 56
try:
    FIONCLEX = 21584
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 57
try:
    FIOCLEX = 21585
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 58
try:
    FIOASYNC = 21586
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 59
try:
    TIOCSERCONFIG = 21587
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 60
try:
    TIOCSERGWILD = 21588
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 61
try:
    TIOCSERSWILD = 21589
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 62
try:
    TIOCGLCKTRMIOS = 21590
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 63
try:
    TIOCSLCKTRMIOS = 21591
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 64
try:
    TIOCSERGSTRUCT = 21592
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 65
try:
    TIOCSERGETLSR = 21593
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 66
try:
    TIOCSERGETMULTI = 21594
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 67
try:
    TIOCSERSETMULTI = 21595
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 69
try:
    TIOCMIWAIT = 21596
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 70
try:
    TIOCGICOUNT = 21597
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 71
try:
    FIOQSIZE = 21598
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 74
try:
    TIOCPKT_DATA = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 75
try:
    TIOCPKT_FLUSHREAD = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 76
try:
    TIOCPKT_FLUSHWRITE = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 77
try:
    TIOCPKT_STOP = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 78
try:
    TIOCPKT_START = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 79
try:
    TIOCPKT_NOSTOP = 16
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 80
try:
    TIOCPKT_DOSTOP = 32
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm/ioctls.h: 82
try:
    TIOCSER_TEMT = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 27
try:
    SIOCADDRT = 35083
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 28
try:
    SIOCDELRT = 35084
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 29
try:
    SIOCRTMSG = 35085
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 32
try:
    SIOCGIFNAME = 35088
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 33
try:
    SIOCSIFLINK = 35089
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 34
try:
    SIOCGIFCONF = 35090
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 35
try:
    SIOCGIFFLAGS = 35091
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 36
try:
    SIOCSIFFLAGS = 35092
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 37
try:
    SIOCGIFADDR = 35093
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 38
try:
    SIOCSIFADDR = 35094
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 39
try:
    SIOCGIFDSTADDR = 35095
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 40
try:
    SIOCSIFDSTADDR = 35096
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 41
try:
    SIOCGIFBRDADDR = 35097
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 42
try:
    SIOCSIFBRDADDR = 35098
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 43
try:
    SIOCGIFNETMASK = 35099
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 44
try:
    SIOCSIFNETMASK = 35100
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 45
try:
    SIOCGIFMETRIC = 35101
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 46
try:
    SIOCSIFMETRIC = 35102
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 47
try:
    SIOCGIFMEM = 35103
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 48
try:
    SIOCSIFMEM = 35104
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 49
try:
    SIOCGIFMTU = 35105
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 50
try:
    SIOCSIFMTU = 35106
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 51
try:
    SIOCSIFNAME = 35107
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 52
try:
    SIOCSIFHWADDR = 35108
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 53
try:
    SIOCGIFENCAP = 35109
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 54
try:
    SIOCSIFENCAP = 35110
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 55
try:
    SIOCGIFHWADDR = 35111
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 56
try:
    SIOCGIFSLAVE = 35113
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 57
try:
    SIOCSIFSLAVE = 35120
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 58
try:
    SIOCADDMULTI = 35121
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 59
try:
    SIOCDELMULTI = 35122
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 60
try:
    SIOCGIFINDEX = 35123
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 61
try:
    SIOGIFINDEX = SIOCGIFINDEX
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 62
try:
    SIOCSIFPFLAGS = 35124
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 63
try:
    SIOCGIFPFLAGS = 35125
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 64
try:
    SIOCDIFADDR = 35126
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 65
try:
    SIOCSIFHWBROADCAST = 35127
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 66
try:
    SIOCGIFCOUNT = 35128
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 68
try:
    SIOCGIFBR = 35136
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 69
try:
    SIOCSIFBR = 35137
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 71
try:
    SIOCGIFTXQLEN = 35138
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 72
try:
    SIOCSIFTXQLEN = 35139
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 77
try:
    SIOCDARP = 35155
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 78
try:
    SIOCGARP = 35156
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 79
try:
    SIOCSARP = 35157
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 82
try:
    SIOCDRARP = 35168
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 83
try:
    SIOCGRARP = 35169
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 84
try:
    SIOCSRARP = 35170
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 88
try:
    SIOCGIFMAP = 35184
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 89
try:
    SIOCSIFMAP = 35185
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 93
try:
    SIOCADDDLCI = 35200
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 94
try:
    SIOCDELDLCI = 35201
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 103
try:
    SIOCDEVPRIVATE = 35312
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctls.h: 109
try:
    SIOCPROTOPRIVATE = 35296
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 36
try:
    NCC = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 48
try:
    TIOCM_LE = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 49
try:
    TIOCM_DTR = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 50
try:
    TIOCM_RTS = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 51
try:
    TIOCM_ST = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 52
try:
    TIOCM_SR = 16
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 53
try:
    TIOCM_CTS = 32
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 54
try:
    TIOCM_CAR = 64
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 55
try:
    TIOCM_RNG = 128
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 56
try:
    TIOCM_DSR = 256
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 57
try:
    TIOCM_CD = TIOCM_CAR
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 58
try:
    TIOCM_RI = TIOCM_RNG
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 63
try:
    N_TTY = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 64
try:
    N_SLIP = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 65
try:
    N_MOUSE = 2
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 66
try:
    N_PPP = 3
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 67
try:
    N_STRIP = 4
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 68
try:
    N_AX25 = 5
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 69
try:
    N_X25 = 6
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 70
try:
    N_6PACK = 7
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 71
try:
    N_MASC = 8
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 72
try:
    N_R3964 = 9
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 73
try:
    N_PROFIBUS_FDL = 10
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 74
try:
    N_IRDA = 11
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 75
try:
    N_SMSBLOCK = 12
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 76
try:
    N_HDLC = 13
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 77
try:
    N_SYNC_PPP = 14
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 78
try:
    N_HCI = 15
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 55
def CTRL(x):
    return (x & 37)

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 56
try:
    CEOF = (CTRL ('d'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 60
try:
    CEOL = '\\0'
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 62
try:
    CERASE = 177
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 63
try:
    CINTR = (CTRL ('c'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 67
try:
    CSTATUS = '\\0'
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 69
try:
    CKILL = (CTRL ('u'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 70
try:
    CMIN = 1
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 71
try:
    CQUIT = 34
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 72
try:
    CSUSP = (CTRL ('z'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 73
try:
    CTIME = 0
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 74
try:
    CDSUSP = (CTRL ('y'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 75
try:
    CSTART = (CTRL ('q'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 76
try:
    CSTOP = (CTRL ('s'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 77
try:
    CLNEXT = (CTRL ('v'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 78
try:
    CDISCARD = (CTRL ('o'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 79
try:
    CWERASE = (CTRL ('w'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 80
try:
    CREPRINT = (CTRL ('r'))
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 81
try:
    CEOT = CEOF
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 83
try:
    CBRK = CEOL
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 84
try:
    CRPRNT = CREPRINT
except:
    pass

# /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/sys/ttydefaults.h: 85
try:
    CFLUSH = CDISCARD
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 192
try:
    OUTPUTS = vmOUTPUTS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 193
try:
    INPUTS = vmINPUTS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 194
try:
    BUTTONS = vmBUTTONS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 195
try:
    LEDS = vmLEDS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 197
try:
    LCD_WIDTH = vmLCD_WIDTH
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 198
try:
    LCD_HEIGHT = vmLCD_HEIGHT
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 199
try:
    TOPLINE_HEIGHT = vmTOPLINE_HEIGHT
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 200
try:
    LCD_STORE_LEVELS = vmLCD_STORE_LEVELS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 204
try:
    FG_COLOR = vmFG_COLOR
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 205
try:
    BG_COLOR = vmBG_COLOR
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 207
try:
    CHAIN_DEPT = vmCHAIN_DEPT
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 209
try:
    EVENT_BT_PIN = vmEVENT_BT_PIN
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 213
try:
    MEMORY_FOLDER = vmMEMORY_FOLDER
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 214
try:
    PROGRAM_FOLDER = vmPROGRAM_FOLDER
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 215
try:
    DATALOG_FOLDER = vmDATALOG_FOLDER
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 216
try:
    SDCARD_FOLDER = vmSDCARD_FOLDER
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 217
try:
    USBSTICK_FOLDER = vmUSBSTICK_FOLDER
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 224
try:
    EXT_SOUND = vmEXT_SOUND
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 225
try:
    EXT_GRAPHICS = vmEXT_GRAPHICS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 226
try:
    EXT_BYTECODE = vmEXT_BYTECODE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 227
try:
    EXT_TEXT = vmEXT_TEXT
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 228
try:
    EXT_DATALOG = vmEXT_DATALOG
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 229
try:
    EXT_PROGRAM = vmEXT_PROGRAM
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 230
try:
    EXT_CONFIG = vmEXT_CONFIG
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 237
try:
    PROJECT = 'LMS2012'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 238
try:
    VERS = 1.04
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 239
try:
    SPECIALVERS = 'H'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 242
try:
    MAX_PROGRAMS = SLOTS
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 243
try:
    MAX_BREAKPOINTS = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 244
try:
    MAX_LABELS = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 245
try:
    MAX_DEVICE_TYPE = 127
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 246
try:
    MAX_VALID_TYPE = vmMAX_VALID_TYPE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 247
try:
    MAX_DEVICE_MODES = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 248
try:
    MAX_DEVICE_DATASETS = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 249
try:
    MAX_DEVICE_DATALENGTH = 32
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 251
try:
    MAX_DEVICE_BUSY_TIME = 1200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 253
try:
    MAX_DEVICE_TYPES = ((MAX_DEVICE_TYPE + 1) * MAX_DEVICE_MODES)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 255
try:
    MAX_FRAMES_PER_SEC = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 257
try:
    CACHE_DEEPT = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 258
try:
    MAX_HANDLES = 250
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 260
try:
    MAX_ARRAY_SIZE = 1000000000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 261
try:
    MIN_ARRAY_ELEMENTS = 0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 263
try:
    INSTALLED_MEMORY = 6000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 264
try:
    RESERVED_MEMORY = 100
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 265
try:
    LOW_MEMORY = 500
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 267
try:
    LOGBUFFER_SIZE = 1000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 268
try:
    DEVICE_LOGBUF_SIZE = 300
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 269
try:
    MIN_LIVE_UPDATE_TIME = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 271
try:
    MIN_IIC_REPEAT_TIME = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 272
try:
    MAX_IIC_REPEAT_TIME = 1000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 274
try:
    MAX_COMMAND_BYTECODES = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 275
try:
    MAX_COMMAND_LOCALS = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 276
try:
    MAX_COMMAND_GLOBALS = 1021
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 278
try:
    UI_PRIORITY = 20
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 279
try:
    C_PRIORITY = 200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 284
try:
    PRG_PRIORITY = 200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 287
try:
    BUTTON_DEBOUNCE_TIME = 30
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 288
try:
    BUTTON_START_REPEAT_TIME = 400
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 289
try:
    BUTTON_REPEAT_TIME = 200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 291
try:
    LONG_PRESS_TIME = 3000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 293
try:
    ADC_REF = 5000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 294
try:
    ADC_RES = 4095
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 296
try:
    IN1_ID_HYSTERESIS = 50
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 297
try:
    OUT5_ID_HYSTERESIS = 100
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 299
try:
    DEVICE_UPDATE_TIME = 1000000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 300
try:
    DELAY_TO_TYPEDATA = 10000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 301
try:
    DAISYCHAIN_MODE_TIME = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 302
try:
    MAX_FILE_HANDLES = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 303
try:
    MIN_HANDLE = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 305
try:
    ID_LENGTH = 7
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 306
try:
    NAME_LENGTH = 12
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 308
try:
    ERROR_BUFFER_SIZE = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 310
try:
    PWM_DEVICE = 'lms_pwm'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 311
try:
    PWM_DEVICE_NAME = '/dev/lms_pwm'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 313
try:
    MOTOR_DEVICE = 'lms_motor'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 314
try:
    MOTOR_DEVICE_NAME = '/dev/lms_motor'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 316
try:
    ANALOG_DEVICE = 'lms_analog'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 317
try:
    ANALOG_DEVICE_NAME = '/dev/lms_analog'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 319
try:
    POWER_DEVICE = 'lms_power'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 320
try:
    POWER_DEVICE_NAME = '/dev/lms_power'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 322
try:
    DCM_DEVICE = 'lms_dcm'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 323
try:
    DCM_DEVICE_NAME = '/dev/lms_dcm'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 325
try:
    UI_DEVICE = 'lms_ui'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 326
try:
    UI_DEVICE_NAME = '/dev/lms_ui'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 328
try:
    LCD_DEVICE = 'lms_display'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 330
try:
    LCD_DEVICE_NAME = '/dev/fb0'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 332
try:
    UART_DEVICE = 'lms_uart'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 333
try:
    UART_DEVICE_NAME = '/dev/lms_uart'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 335
try:
    USBDEV_DEVICE = 'lms_usbdev'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 336
try:
    USBDEV_DEVICE_NAME = '/dev/lms_usbdev'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 338
try:
    USBHOST_DEVICE = 'lms_usbhost'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 339
try:
    USBHOST_DEVICE_NAME = '/dev/lms_usbhost'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 341
try:
    SOUND_DEVICE = 'lms_sound'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 342
try:
    SOUND_DEVICE_NAME = '/dev/lms_sound'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 344
try:
    IIC_DEVICE = 'lms_iic'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 345
try:
    IIC_DEVICE_NAME = '/dev/lms_iic'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 347
try:
    BT_DEVICE = 'lms_bt'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 348
try:
    BT_DEVICE_NAME = '/dev/lms_bt'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 350
try:
    UPDATE_DEVICE = 'lms_update'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 351
try:
    UPDATE_DEVICE_NAME = '/dev/lms_update'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 353
try:
    TEST_PIN_DEVICE = 'lms_tst_pin'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 354
try:
    TEST_PIN_DEVICE_NAME = '/dev/lms_tst_pin'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 356
try:
    TEST_UART_DEVICE = 'lms_tst_uart'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 357
try:
    TEST_UART_DEVICE_NAME = '/dev/lms_tst_uart'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 360
try:
    DIR_DEEPT = vmDIR_DEEPT
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 367
try:
    FILENAMESIZE = vmFILENAMESIZE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 368
try:
    FILENAME_SIZE = 52
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 369
try:
    FOLDERNAME_SIZE = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 370
try:
    SUBFOLDERNAME_SIZE = FILENAME_SIZE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 372
try:
    MAX_FILENAME_SIZE = (((FOLDERNAME_SIZE + SUBFOLDERNAME_SIZE) + FILENAME_SIZE) + 5)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 376
try:
    TYPEDATE_FILE_NAME = 'typedata'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 377
try:
    ICON_FILE_NAME = 'icon'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 378
try:
    TEXT_FILE_NAME = 'text'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 380
try:
    DEMO_FILE_NAME = '../prjs/BrkProg_SAVE/Demo.rpf'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 394
try:
    SDCARD_DEVICE1 = '/dev/mmcblk0'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 395
try:
    SDCARD_DEVICE2 = '/dev/mmcblk0p1'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 398
try:
    SDCARD_MOUNT = './mount_sdcard'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 399
try:
    SDCARD_UNMOUNT = './unmount_sdcard'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 404
try:
    USBSTICK_DEVICE = '/dev/sda'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 409
try:
    USBSTICK_MOUNT = './mount_usbstick'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 410
try:
    USBSTICK_UNMOUNT = './unmount_usbstick'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 422
try:
    DEFAULT_FOLDER = 'ui'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 423
try:
    DEFAULT_UI = 'ui'
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 425
try:
    DEFAULT_VOLUME = vmDEFAULT_VOLUME
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 426
try:
    DEFAULT_SLEEPMINUTES = vmDEFAULT_SLEEPMINUTES
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 428
try:
    COM_CMD_DEVICE_NAME = USBDEV_DEVICE_NAME
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 447
try:
    BATT_INDICATOR_HIGH = 7500
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 448
try:
    BATT_INDICATOR_LOW = 6200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 450
try:
    ACCU_INDICATOR_HIGH = 7500
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 451
try:
    ACCU_INDICATOR_LOW = 7100
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 463
try:
    LOW_VOLTAGE_SHUTDOWN_TIME = 10000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 465
try:
    BATT_WARNING_HIGH = 6.2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 466
try:
    BATT_WARNING_LOW = 5.5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 467
try:
    BATT_SHUTDOWN_HIGH = 5.5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 468
try:
    BATT_SHUTDOWN_LOW = 4.5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 470
try:
    ACCU_WARNING_HIGH = 7.1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 471
try:
    ACCU_WARNING_LOW = 6.5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 472
try:
    ACCU_SHUTDOWN_HIGH = 6.5
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 473
try:
    ACCU_SHUTDOWN_LOW = 6.0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 512
try:
    TEMP_SHUTDOWN_FAIL = 45.0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 513
try:
    TEMP_SHUTDOWN_WARNING = 40.0
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 521
try:
    UPDATE_TIME1 = 2
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 522
try:
    UPDATE_TIME2 = 10
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 523
try:
    UPDATE_MEMORY = 200
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 524
try:
    UPDATE_SDCARD = 500
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 525
try:
    UPDATE_USBSTICK = 500
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 529
try:
    MAX_SOUND_DATA_SIZE = 250
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 530
try:
    SOUND_CHUNK = 250
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 531
try:
    SOUND_ADPCM_CHUNK = 125
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 532
try:
    SOUND_MASTER_CLOCK = 132000000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 533
try:
    SOUND_TONE_MASTER_CLOCK = 1031250
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 534
try:
    SOUND_MIN_FRQ = 250
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 535
try:
    SOUND_MAX_FRQ = 10000
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 536
try:
    SOUND_MAX_LEVEL = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 537
try:
    SOUND_FILE_BUFFER_SIZE = (SOUND_CHUNK + 2)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 538
try:
    SOUND_BUFFER_COUNT = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 539
try:
    SOUND_FILE_FORMAT_NORMAL = 256
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 540
try:
    SOUND_FILE_FORMAT_COMPRESSED = 257
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 550
def VtoC(V):
    return ((V * ADC_RES) / ADC_REF)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 551
def CtoV(C):
    return ((C * ADC_REF) / ADC_RES)

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 552
def MtoV(M):
    return (((M * ADC_REF) * 100) / (ADC_RES * 52))

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 554
try:
    KB = 1024
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 769
try:
    TYPE_NAME_LENGTH = 11
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 770
try:
    SYMBOL_LENGTH = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 800
try:
    TYPE_PARAMETERS = 19
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 801
try:
    MAX_DEVICE_INFOLENGTH = 54
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 922
try:
    ERR_STRING_SIZE = vmERR_STRING_SIZE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 930
try:
    COLORS = 4
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 931
try:
    CALPOINTS = 3
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1027
try:
    UART_DATA_LENGTH = MAX_DEVICE_DATALENGTH
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1028
try:
    UART_BUFFER_SIZE = 64
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1054
try:
    UART_PORT_CHANGED = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1055
try:
    UART_DATA_READY = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1056
try:
    UART_WRITE_REQUEST = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1094
try:
    IIC_DATA_LENGTH = MAX_DEVICE_DATALENGTH
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1095
try:
    IIC_NAME_LENGTH = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1122
try:
    IIC_PORT_CHANGED = 1
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1123
try:
    IIC_DATA_READY = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1124
try:
    IIC_WRITE_REQUEST = 16
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1175
try:
    TST_PIN_LENGTH = 8
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1193
try:
    TST_UART_LENGTH = UART_BUFFER_SIZE
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1238
try:
    LCD_BUFFER_SIZE = (((LCD_WIDTH + 7) / 8) * LCD_HEIGHT)
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1239
try:
    LCD_TOPLINE_SIZE = (((LCD_WIDTH + 7) / 8) * (TOPLINE_HEIGHT + 1))
except:
    pass

# /home/pikachu/ev3/ev3sources/lms2012/lms2012/source/lms2012.h: 1420
try:
    PRINTBUFFERSIZE = 160
except:
    pass

timespec = struct_timespec # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/time.h: 121

timeval = struct_timeval # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/time.h: 69

__pthread_internal_slist = struct___pthread_internal_slist # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 48

__pthread_mutex_s = struct___pthread_mutex_s # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/pthreadtypes.h: 58

winsize = struct_winsize # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 28

termio = struct_termio # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/bits/ioctl-types.h: 37

# No inserted files

