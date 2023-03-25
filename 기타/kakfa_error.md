# Kakfa Error

## Caused by: java.lang.UnsatisfiedLinkError: no tibftljni in java.library.path
Java.library.path tibftljni가 없다고 알려주는 에러

### 해결 방법

```
$ source ~/.bashrc
$ 
$ LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:{tibftljni가 있는 경로 지정}
$ 
$ export LD_LIBRARY_PATHb

```

$ source ~/.bahsrc




