from MCSL2Lib.variables import BaseServerVariables
from PyQt5.QtCore import QObject


class ServerValidator(QObject):
    def __init__(self):
        super().__init__()

    def checkJavaSet(self, v: BaseServerVariables):
        """检查Java设置"""
        if v.selectedJavaPath != "":
            return self.tr("Java检查: 正常"), 0
        else:
            return self.tr("Java检查: 出错，缺失"), 1

    def checkMemSet(self, minMem, maxMem, v: BaseServerVariables):
        """检查内存设置"""

        # 是否为空
        if minMem != "" and maxMem != "":
            # 是否是数字
            if minMem.isdigit() and maxMem.isdigit():
                # 是否为整数
                if not int(minMem) % 1 and not int(maxMem) % 1:
                    # 是否为整数
                    if int(minMem) <= int(minMem):
                        v.minMem = int(minMem)
                        v.maxMem = int(maxMem)
                        return self.tr("内存检查: 正常"), 0

                    else:
                        return self.tr("内存检查: 出错, 最小内存必须小于等于最大内存"), 1
                else:
                    return self.tr("内存检查: 出错, 不为整数"), 1
            else:
                return self.tr("内存检查: 出错, 不为数字"), 1
        else:
            return self.tr("内存检查: 出错, 内容为空"), 1

    def checkCoreSet(self, v: BaseServerVariables):
        """检查核心设置"""
        if v.coreFileName != "":
            return self.tr("核心检查: 正常"), 0
        else:
            return self.tr("核心检查: 出错，缺失"), 1

    def checkServerNameSet(self, n, v: BaseServerVariables):
        """检查服务器名称设置"""
        errText = self.tr("服务器名称检查: 出错")
        isError: int
        illegalServerCharacterList = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]
        illegalServerNameList = [
            "aux",
            "prn",
            "con",
            "lpt1",
            "lpt2",
            "nul",
            "com0",
            "com1",
            "com2",
            "com3",
            "com4",
            "com5",
            "com6",
            "com7",
            "com8",
            "com9",
        ]
        for i in range(len(illegalServerNameList)):
            if illegalServerNameList[i] == n:
                errText += self.tr("，名称与操作系统冲突")
                isError = 1
                break
            else:
                isError = 0
        for eachIllegalServerCharacter in illegalServerCharacterList:
            if eachIllegalServerCharacter not in n:
                pass
            else:
                errText += self.tr("，名称含有不合法字符")
                isError = 1
                break
        if n == "":
            errText += self.tr("，未填写")
            isError = 1
        if isError == 1:
            return errText, isError
        else:
            v.serverName = n
            return self.tr("服务器名称检查: 正常"), isError

    def checkJVMArgSet(self, j, v: BaseServerVariables):
        """检查JVM参数设置，同时设置"""
        if j != "":
            v.jvmArg = j.split(" ")
            return self.tr("JVM参数检查：正常"), 0
        else:
            v.jvmArg = ["-Dlog4j2.formatMsgNoLookups=true"]
            return self.tr("JVM参数检查：正常（无手动参数，自动启用log4j2防护）"), 0

    def checkMemUnitSet(self):
        """检查JVM内存堆单位设置"""
        return self.tr("JVM内存堆单位检查：正常"), 0

    def checkIconSet(self):
        """检查图标设置"""
        return self.tr("图标检查：正常"), 0