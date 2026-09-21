# Contribution & Collaboration Log

This project was developed through a collaborative workflow between human reasoning and AI assistance (Gemini / ChatGPT). Below is the breakdown of responsibilities and contributions.

## 🧑‍💻 Human Contribution (Ketan Gajanan Toraskar)

* **Experimental Execution:** Ran profiling commands using `py-spy` under elevated administrator privileges.

* **Troubleshooting & Optimization:** Identified timing anomalies ($0.06\text{ ms}$ runtimes caused by insufficient workloads) and determined scale requirements ($1000 \times 1000$ grid) to achieve recordable sampling durations ($\sim 3\text{--}4\text{ seconds}$).

* **Data Collection & Verification:** Executed multiple profiling runs, recorded raw terminal output metrics, verified node expansion counts, and checked generated `.svg` flame graphs.

* **Report & Analysis:** Authored final analytical justifications, analyzed time versus state-space complexity trade-offs, and structured docx assignment files.

## 🤖 AI Contribution (Gemini)

* **Script Development:** Provided initial boilerplate code for Dijkstra's and A\* search algorithms with Euclidean heuristic logic.

* **Profiler Integration:** Provided exact `py-spy` command syntax and execution parameters for cross-platform support.

* **Formatting & Templating:** Structured Markdown tables, contribution logs, and Word formatting configurations (`python-docx`).

* **Debugging Assistance:** Assisted in revising grid scale settings and iteration counters to ensure sampling viability.

## ⚖️ Ethical AI Declaration

AI tools were used as a pair-programming and troubleshooting assistant. All experimental measurements, flame graph logs, execution commands, and final analytical evaluations were independently executed, validated, and verified.