import pyperclip

saikikeisatu = [
"                            *     *          *                           ",
" ***********    * ******   ***********  ***********      *    *        * ",
"      *       * * ******    ******* *   * *       *     **   * *       * ",
"  *********   * *      *   **** *  **   * *********  ******            * ",
"  *   *   *   * * ******    ****         ** * * *       *              * ",
"  *   *   *   * *            *******    ** *   **       *  ****        * ",
"  *********   * *********  ***********    ********     *               * ",
"  *   *   *     * *******    *******    **       **    *               * ",
" ***********    * *  * *     *******     *********    **                 ",
"  *       *    *  *  * *    *********        * *      *   *            * ",
"  *       *    *  *  ***    *       *     *  *  **   **    *****       * ",
"  *     ***   *      *      *********   ** ***   *                       ",
]


from typing import List
with open("answer.py", "r", encoding="utf-8") as f:
    lines: List[str] = f.readlines()
    dfsflag = False
    codonflag = False
    pypyflag = False
    for line in lines:
        if "dfs" in line: dfsflag = True
        if "@extend" in line: codonflag = True
        if "pypy" in line: pypyflag = True

    if dfsflag and not codonflag and not pypyflag:
        for s in saikikeisatu:
            print(s)
        print("Detected \"dfs\". Might need a spell. Copied.")
    text = "".join(lines)
    pyperclip.copy(text)