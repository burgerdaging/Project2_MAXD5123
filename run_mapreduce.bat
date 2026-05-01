@echo off
REM ============================================
REM  Simulated Hadoop MapReduce on Windows
REM  Pipes: input -> mapper -> sort -> reducer -> output
REM ============================================

echo Running MapReduce job...
echo.

if not exist screenshots mkdir screenshots

type dataset\TitanicData.txt | python mapreduce\mapper.py | sort | python mapreduce\reducer.py > screenshots\mapreduce_output.txt

echo ===== RESULT =====
type screenshots\mapreduce_output.txt
echo ==================
echo.
echo Output saved to: screenshots\mapreduce_output.txt