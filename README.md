# K3 Track 1 · Day 20–21 — AI Evaluation (eval-kit)

## 📌 Thông tin Cá nhân & Nhóm
- **Học viên:** Đinh Lê Quỳnh Phương (MSSV: 2A202601865)
- **Nhóm:** Nhóm Hihi (Gồm: Đinh Lê Quỳnh Phương & Cao Các Tường)
- **Sản phẩm đánh giá:** VLearn AI Tutor (AI Assistant cho khóa học AI Evaluations)
- **Repository nộp bài:** [K3-Track1-Day20-21-AI-Evaluation-2A202601865_DinhLeQuynhPhuong](https://github.com/quynhphuong1209/K3-Track1-Day20-21-AI-Evaluation-2A202601865_DinhLeQuynhPhuong)

---

## 🗺️ Sơ đồ 6 Phase & Artifacts từng Phase

```mermaid
graph TD
    P1["Phase 1: Coverage & Input Grid"] --> A1["dataset-v1.jsonl (20 scenarios)"]
    P2["Phase 2: Human Baseline"] --> A2["labels-phuong.csv, labels-tuong.csv -> labels.csv (100% Consensus)"]
    P3["Phase 3: Rubric & Routing Architecture"] --> A3["Rubric v1 (5 tiêu chí) & Routing 4 Làn"]
    P4["Phase 4: Calibration LLM Judge"] --> A4["judge-prompt-v1.md -> judge-prompt-v2.md & verdicts-v2.jsonl (100% Agreement)"]
    P5["Phase 5: Scorecard & Pre-set Quality Gates"] --> A5["Scorecard 9 tiêu chí & Slice Breakdown"]
    P6["Phase 6: Verdict & PM Final Report"] --> A6["REPORT.md (Mục 1..7) & ai-log.md"]
```

### Artifacts tương ứng theo từng Phase:
1. **Phase 1 (Coverage & Input Grid):** `deliverables/REPORT.md#1-input-grid` & `deliverables/evidence/dataset-v1.jsonl`
2. **Phase 2 (Human Baseline):** `deliverables/evidence/labels.csv` (Agreement ban đầu: 80.0%, Nhãn đồng thuận: 19 Pass, 1 Fail)
3. **Phase 3 (Rubric & Routing Map):** `deliverables/REPORT.md#3-rubric-v1` (Rubric 5 tiêu chí) & `deliverables/REPORT.md#4-routing-map` (Kiến trúc 4 làn: Code Check -> LLM Judge -> LLM Assist -> Expert Review)
4. **Phase 4 (Scale & Calibrate Judge):** 
   - Vòng 1 (Baseline): `deliverables/evidence/judge-prompt-v1.md` & `deliverables/evidence/verdicts-v1.jsonl` (Agreement 90.0%, TPR 94.7%, TNR 0%)
   - Vòng 2 (Calibrated): `deliverables/evidence/judge-prompt-v2.md` & `deliverables/evidence/verdicts-v2.jsonl` (Agreement **100.0%**, TPR **100.0%**, TNR **100.0%**)
5. **Phase 5 (Scorecard & Pre-set Gates):** `deliverables/REPORT.md#6-scorecard--gate` (Scorecard 9 tiêu chí, Latency 7.2s/câu, Cost $0.005/vòng)
6. **Phase 6 (Verdict & PM Report):** `deliverables/REPORT.md#7-verdict--report-cuối` & `ai-log.md`

---

## 👤 Đóng góp Cá nhân (Đinh Lê Quỳnh Phương)
- **Phụ trách chính:**
  1. Xây dựng và mở rộng làn Code Check trong `eval/code_checks.py` từ 3 rules lên **5 rules** (`schema_valid`, `citation_exists`, `quote_verbatim`, `scope_valid`, `refusal_sources_empty`), kiểm thử tự động 100% free API.
  2. Thực hiện gán nhãn độc lập Vòng 1 cho 20 scenarios (`labels-phuong.csv`), tham gia thảo luận phân tích 4 ca bất đồng và thống nhất bộ nhãn vàng `labels.csv`.
  3. Phân tích chi tiết lỗi sai số Vòng 1 (False Negative ở `sc-03` do quote ngắn & False Positive ở `sc-20` do over-generation khi input rỗng).
  4. Hiệu chuẩn prompt sang `judge-prompt-v2.md` bổ sung 2 quy tắc giải mã (*Quote rút gọn* & *Câu hỏi rỗng/cụt*) và 2 ví dụ Near-Miss, nâng tỷ lệ đồng thuận lên **100% (20/20)**.
  5. Đóng góp xây dựng báo cáo `REPORT.md` (Mục 1..7) và viết file `ai-log.md` cá nhân.

---

## 🎯 Verdict của Nhóm & Lý do
- **Quyết định:** **SHIP WITH CONDITIONS** (Đủ điều kiện phát hành kèm 1 điều kiện sửa System Prompt).
- **Căn cứ bằng chứng:**
  - **Code Check (Deterministic Blockers):** Đạt **100% Pass** trên 5 quy tắc cứng.
  - **Bảo mật & Ranh giới (Refusal & Safety):** Đạt **100% Pass** — bảo vệ tuyệt đối trước Prompt Injection (`sc-18`), từ chối xin đáp án Capstone (`sc-17`), không bịa nguồn giả (`sc-19`).
  - **Giải mã ngữ cảnh Slide (Deixis Resolution):** Đạt **100% Pass** (5/5 câu hỏi mơ hồ).
  - **Độ bám nguồn (Groundedness):** Đạt **95.0% Pass** (19/20 câu), vượt ngưỡng Hard Gate ≥ 90%.
- **Điều kiện duy nhất trước khi bật traffic thật:** Bổ sung 1 câu quy tắc vào System Prompt của Tutor (`tutor/tutor.py`): *"Nếu câu hỏi của học viên quá ngắn hoặc chỉ có 1 từ vô nghĩa mà không có context slide (như sc-20 'Hỏi?'), bắt buộc phải chào hỏi và yêu cầu người dùng làm rõ câu hỏi, không tự ý xả bài giảng lý thuyết dài"*.

---

## 💡 Bài học mang về áp dụng cho dự án thật
1. **Tư duy "Chưa Calibrate Judge thì Chưa được phép tin Judge":** Không bao giờ tin tưởng hoàn toàn vào phán quyết của LLM Judge khi chưa có nhãn vàng của con người và chưa đo lường ma trận nhầm lẫn (TPR/TNR).
2. **Thiết kế Routing 4 Làn tối ưu:** Đẩy tối đa các kiểm tra logic cứng xuống **Code Check (Deterministic)** giúp kiểm tra cực nhanh, hoàn toàn miễn phí (0$ API) trước khi gọi LLM Judge.
3. **Khóa Ngưỡng Gate TRƯỚC khi xem số (Pre-set Quality Gates):** Không đưa ra quyết định dựa trên cảm tính ("78% cũng ổn"); phải chốt cứng Hard Gates và Soft Gates từ đầu để đánh giá khách quan.

---

## Cấu trúc repo

| Thư mục / file | Vai trò |
|---|---|
| `tutor/` | **Sản phẩm đang được đánh giá** — tutor thật (`tutor.py`: system prompt + tool-calling `kb_search`, BM25 retrieval) và `corpus/` 18 tài liệu nguồn + `manifest.json` (địa chỉ nguồn: `doc_id#section_id`) |
| `eval/` | **Bộ máy chấm** — code chạy & phân tích eval + tracking: `run_eval.py`, `code_checks.py`, `judge.py`, `agreement.py`, `report.py`, `tracing.py`, kèm `judge_prompt.md` (prompt judge — **file bạn sẽ sửa nhiều nhất khi calibrate**) |
| `deliverables/` | **Khung bài nộp** — report log A→Z, lock input/output/quyết định từng bước: `REPORT.md` một file gồm 7 mục quyết định theo phase (1 Input Grid … 7 Verdict) + `evidence/` chứa data thô dẫn chứng (xem README trong đó) |
| `tests/` | `test_eval_kit.py` — 44 test offline (không tốn API), chạy trước khi làm bất cứ thứ gì |
| `data/` | File mẫu: `dataset.example.jsonl` (5 câu đủ loại: in-scope, out-of-scope, mơ hồ, xin đáp án) và `labels.example.csv` (format nhãn người) |
| root | File làm việc (scratch) bạn sinh ra khi chạy: `dataset.jsonl`, `results.jsonl`, `verdicts.jsonl`, `labels.csv`, `report.html` (đã gitignore, không commit) |

**Mọi lệnh đều chạy từ root repo** (thư mục chứa README này). Luồng làm việc: file
scratch sinh ra ở root → chốt một vòng thì copy vào `deliverables/evidence/`, đặt tên
theo version (`results-v1.jsonl`, `verdicts-v2.jsonl`...), không ghi đè vòng cũ.

## Quickstart (3 phút)

```bash
pip install -r requirements.txt        # 1. cài đặt (chỉ cần requests; braintrust/langsmith để tracing)
cp .env.example .env                   # 2. điền API key của provider bạn dùng (+ BRAINTRUST_API_KEY hoặc LANGSMITH_API_KEY để log trace)
cp data/dataset.example.jsonl dataset.jsonl
python3 tests/test_eval_kit.py         # 3. 44 test offline phải sạch hết
python3 eval/run_eval.py                # 4. chạy tutor trên dataset -> results.jsonl
python3 eval/report.py && open report.html   # 5. xem kết quả, gán nhãn
```

Gợi ý: nếu test fail ngay tầng 2 (corpus), gần như chắc chắn bạn đang chạy sai thư mục —
`cd` vào đúng root repo rồi chạy lại.

## Làm bài theo 6 phase — bước nào chạy gì?

| Phase (theo file lab tổng) | Làm ở đâu | Trong repo này chạy gì |
|---|---|---|
| **P1. Thiết kế coverage** — chọn dimensions, tổ hợp, sinh câu hỏi | Giấy/sheet + AI chat | Chưa cần repo. Kết quả: viết vào `dataset.jsonl` (format xem `data/dataset.example.jsonl`, nhớ field `metadata.slide`) |
| **P2. Human baseline** — chạy dataset, chấm tay | Repo | `python3 eval/run_eval.py` → `python3 eval/report.py` → mở `report.html` gán nhãn → Export `labels-<tên>.csv` → `python3 eval/agreement.py labels-*.csv` đo đồng thuận |
| **P3. Rubric + routing** | Thảo luận nhóm | Không chạy repo. Viết vào mục 3 (Rubric v1) và mục 4 (Routing Map) trong `deliverables/REPORT.md` |
| **P4. Scale & calibrate judge** | Repo | `python3 eval/code_checks.py` (làn code) → sửa `eval/judge_prompt.md` → `python3 eval/judge.py` → đọc confusion matrix + % agreement. Sửa ít một thứ, chạy lại — mỗi vòng copy `eval/judge_prompt.md` + `verdicts.jsonl` ra `deliverables/evidence/` |
| **P5. Đọc kết quả, đặt ngưỡng** | Repo | `results.jsonl` có sẵn latency/tokens/cost từng câu; `report.html` để đọc theo slice |
| **P6. Verdict + report** | Viết trong `deliverables/` | Điền mục 6 (Scorecard & Gate) và mục 7 (Verdict) trong `deliverables/REPORT.md` |

**Nguyên tắc nộp bài:** mỗi bước phải nộp đủ **đầu vào + đầu ra (data thô) + quyết định
kèm vì sao**. Cấu trúc thư mục nộp và checklist: [deliverables/README.md](deliverables/README.md).

**Tracing bắt buộc:** đặt `BRAINTRUST_API_KEY` hoặc `LANGSMITH_API_KEY` trong `.env`
trước khi chạy — mọi run tutor/judge log thành trace, link project là một phần bài nộp.

## Chi tiết từng lệnh

```bash
python3 eval/run_eval.py      # 1. chạy tutor trên dataset.jsonl      -> results.jsonl
python3 eval/code_checks.py   # 2. làn code: rule thuần Python trên results (không tốn API)
python3 eval/report.py        # 3. sinh report.html -> mở, gán nhãn người, Export labels.csv
python3 eval/agreement.py labels-*.csv   # 4. đo đồng thuận giữa các thành viên
python3 eval/judge.py         # 5. judge chấm theo judge_prompt.md -> verdicts.jsonl + confusion matrix
```

Mỗi lệnh ghi đè file output của nó — muốn giữ vòng cũ, copy file đi trước
(vd `cp results.jsonl deliverables/evidence/results-v1.jsonl`).

Chỉ chấm vài câu: `python3 eval/judge.py sc-01 sc-03`.
Chạy dataset khác: `python3 eval/run_eval.py ten-file.jsonl`.

### Bước 1 — `eval/run_eval.py`: tutor thật chạy trên dataset

- Đọc từng dòng `dataset.jsonl`, gọi tutor theo **cơ chế tool-calling thật**:
  model tự quyết định gọi `kb_search` bao nhiêu lần, với truy vấn nào (xem trong
  `results.jsonl`, trường `tool_calls`).
- In từng dòng: thời gian, số token, chi phí ước tính. Tổng chi phí in ở cuối.
- Gợi ý: chạy thử `data/dataset.example.jsonl` (5 câu) trước khi chạy dataset lớn của nhóm.

### Bước 2 — `eval/code_checks.py`: làn code

- 3 rule có sẵn: `schema_valid` (JSON đủ 4 field), `citation_exists` (doc_id/section_id
  có thật trong corpus), `quote_verbatim` (quote nằm đúng trong section đã cite).
- Mở `eval/code_checks.py`, thêm 1–2 hàm `check_*` của riêng nhóm cho tiêu chí làn Code.

### Bước 3 — `eval/judge.py`: LLM judge chấm

- Judge là model KHÁC tutor (mặc định `gpt-4o-mini`) — tránh tự chấm chéo.
- Rubric judge nằm trong `eval/judge_prompt.md` — **đây là file bạn sẽ sửa nhiều nhất** khi
  calibrate. Sửa ít một thứ mỗi vòng, chạy lại, so agreement.
- Chấm một vài câu thôi: `python3 eval/judge.py sc-01 sc-03`.
- Nếu `labels.csv` đã có nhãn người (export từ report), judge.py in luôn confusion matrix
  + % agreement — **đây là con số calibration của bạn**.

### Bước 4 — `eval/report.py`: nhìn và gán nhãn

- `report.html` tự chứa mọi dữ liệu: câu hỏi, slide context, câu trả lời, nguồn trích,
  verdict judge. Bấm pass/fail/uncertain và nhập **note ngắn** (vd tiêu chí gây
  fail: `fail: citation`) để gán nhãn người (lưu trong trình duyệt).
- Bấm **Export labels.csv** → lưu đè `labels.csv` → chạy lại `eval/judge.py` để xem agreement.

### Những việc mổ xẻ sâu hơn

| Việc | Làm sao |
|---|---|
| Xem tutor gọi `kb_search` với truy vấn gì, bao nhiêu vòng | Mở `results.jsonl`, trường `tool_calls` và `steps` của từng row |
| Sửa retrieval (BM25, top-k) để thử nghiệm | Sửa `retrieve_corpus()` trong `tutor/tutor.py` |
| Đọc system prompt thật của tutor | Đầu file `tutor/tutor.py` — biến `SYSTEM_PROMPT` |
| Chạy judge bằng model khác để so sánh | `EVAL_JUDGE_MODEL=deepseek/deepseek-v4-flash python3 eval/judge.py` |
| Xem raw output chưa parse (khi JSON vỡ) | `results.jsonl` trường `raw_content`; report.html nút "xem raw" |
| Test offline toàn bộ pipeline | `python3 tests/test_eval_kit.py` (không tốn API) |

## Chọn model & provider

Model viết dạng `provider/model` — repo gọi **thẳng API chuẩn của từng hãng**:

| Prefix model | Cần key trong .env |
|---|---|
| `openai/gpt-4o-mini`, ... | `OPENAI_API_KEY` |
| `deepseek/deepseek-v4-flash`, ... | `DEEPSEEK_API_KEY` |
| `gemini/gemini-3.1-flash-lite`, ... | `GEMINI_API_KEY` |
| `anthropic/claude-...` | `ANTHROPIC_API_KEY` |
| `openrouter/<vendor>/<model>` | `OPENROUTER_API_KEY` |

| Biến | Mặc định | Ý nghĩa |
|---|---|---|
| `EVAL_MODEL` | `deepseek/deepseek-v4-flash` | Model của tutor |
| `EVAL_JUDGE_MODEL` | `openai/gpt-4o-mini` | Model của judge (nên KHÁC tutor — tránh tự chấm chéo) |
| `BRAINTRUST_API_KEY` | — | Bật log trace lên Braintrust (bắt buộc một trong hai khi nộp bài) |
| `LANGSMITH_API_KEY` | — | Bật log trace lên LangSmith (thay cho Braintrust; `LANGCHAIN_API_KEY` cũng được) |
| `EVAL_BASE_URL` + `EVAL_API_KEY` | — (không đặt = gọi thẳng provider) | Tuỳ chọn: gateway OpenAI-compatible riêng |

## Tracing (bắt buộc khi nộp bài)

Mọi run tutor/judge phải được log trace — đây là minh chứng bạn chạy thật.

- **Braintrust:** tạo project (vd `ai-evaluation`) trên braintrust.dev, lấy API key, đặt
  vào `.env`: `BRAINTRUST_API_KEY=sk-...`. Từ đó `run_eval.py` và `judge.py` tự log mỗi
  câu thành một trace (input, output, tool calls, tokens, cost).
- **LangSmith:** tạo project trên smith.langchain.com, lấy API key, đặt vào `.env`:
  `LANGSMITH_API_KEY=lsv2_pt_...` (tuỳ chọn `LANGSMITH_PROJECT=ai-evaluation`).
  Code tự nhận backend — không cần sửa gì thêm. Chỉ cần một trong hai.

Khi nộp: ghi link project (Braintrust hoặc LangSmith) vào `deliverables/evidence/braintrust-link.md`.

## Định dạng một dòng dataset

```json
{"scenario_id": "sc-01-in-judge", "input": "câu hỏi của học viên",
 "expected_scope": "in_scope", "note": "ghi chú ngắn của nhóm",
 "metadata": {"slide": {"id": "s53", "title": "Pass rate giống nhau — không có nghĩa judge nghĩ giống bạn",
                        "keyword": "calibration"}}}
```

- `input` là bắt buộc — câu hỏi như học viên thật viết. `scenario_id` là mã duy nhất
  của row (code cũng chấp nhận `id`, nhưng hãy dùng `scenario_id` cho thống nhất —
  xem mẫu `data/dataset.example.jsonl`).
- `expected_scope` / `note` (tuỳ chọn): kỳ vọng in-scope/out-of-scope và ghi chú của nhóm.
- Các thông tin grid (`dimension_values`, `expected_behavior`, `risk_if_fail`,
  `set_type`...) đặt trong `metadata` để sau lọc theo slice.
- `metadata.slide` (khi câu gắn slide) là slide học viên đang xem khi hỏi — đưa vào
  prompt tutor và cả judge, để câu deixis kiểu "giải thích đoạn này" chấm được đúng
  bối cảnh. Câu noise/out-of-scope không gắn slide thì bỏ field này.

## Gỡ lỗi nhanh

| Triệu chứng | Nguyên nhân thường gặp |
|---|---|
| `Chưa có API key...` | Thiếu `.env`, hoặc tên biến sai family (deepseek cần `DEEPSEEK_API_KEY`) |
| Row có `_parse_error` / `_truncated` | Model trả JSON vỡ (thường do cắt output) — mở `raw_content` xem; đó là một failure mode thật, đáng ghi vào bài |
| Judge toàn 401 | Sai key cho provider của model judge (xem bảng provider ở trên), hoặc shell đang export sẵn `OPENAI_API_KEY` khác — kiểm tra `env \| grep OPENAI` |
| Retrieve trượt chủ đề | Câu hỏi quá ngắn/deixis — gắn `metadata.slide` với `keyword` vào row dataset |

## Nộp bài thì lấy gì từ repo?

Quy cách nộp đầy đủ: **[deliverables/README.md](deliverables/README.md)** (đã align với mục 10
của file lab tổng). Từ repo này, copy sang `deliverables/evidence/` của bài nộp:

- `dataset.jsonl` → `deliverables/evidence/dataset-v1.jsonl` — dataset nhóm chốt (đầu vào).
- `results.jsonl` → `deliverables/evidence/results-v1.jsonl` (v2, v3... mỗi lần chạy lại) — output
  tutor thật, có cả `tool_calls`, tokens, cost từng câu.
- `verdicts.jsonl` → `deliverables/evidence/verdicts-v1.jsonl` (v2... từng vòng calibration).
- `eval/judge_prompt.md` → `deliverables/evidence/judge-prompt-v1.md` (copy MỖI LẦN trước khi sửa).
- `labels.csv` (export từ report.html) → `deliverables/evidence/labels.csv` — nhãn người.
- Số liệu agreement/confusion matrix in ra từ `eval/judge.py` → chép vào
  mục 5 của `deliverables/REPORT.md`.

Nhớ: chạy xong một vòng là copy ngay — cuối buổi mới gom là mất dấu các vòng trước.

## Lưu ý

- Model deepseek v4 được gửi kèm `"thinking": {"type": "disabled"}` (đã xử lý sẵn trong
  `tutor/tutor.py`) — thiếu nó output sẽ bị reasoning tokens ăn mất.
- Tutor chạy `max_tokens=2000`: câu dài bị cắt giữa JSON sẽ được đánh dấu
  `_truncated`/`_parse_error` trong `results.jsonl` — đó là một failure mode thật,
  đáng ghi vào bài, đừng xoá.
- Provider thỉnh thoảng trả HTTP 200 nhưng body JSON bị cắt ngang — `chat()` tự retry
  tối đa 3 lần.
- `.env` trong repo được nạp **ghi đè** biến shell sẵn có — nếu shell bạn export sẵn
  `OPENAI_API_KEY` khác thì `.env` vẫn thắng.
- `report.py` không gọi mạng; `report.html` nhúng sẵn toàn bộ dữ liệu.
- Giá token dùng để ước tính chi phí nằm trong `eval/run_eval.py` (biến `PRICING`).
