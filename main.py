<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>석리송 선생님의 API 특강</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;600;800;900&family=IBM+Plex+Mono:wght@400;600&family=Outfit:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#f8f6f1;--card:#fff;--text:#1a1a2e;--dim:#7a7a8e;--border:#e0ddd6;
  --client:#3b6df5;--client-bg:#eef2ff;
  --yt:#e33;--yt-bg:#fff0f0;
  --cl:#d97706;--cl-bg:#fef9ee;
  --api:#8b5cf6;--api-bg:#f3f0ff;
  --green:#10b981;--green-bg:#ecfdf5;
  --red:#ef4444;
  --code-bg:#1e1e2e;--code-text:#cdd6f4;
}
body{background:var(--bg);color:var(--text);font-family:'Noto Sans KR',sans-serif;overflow-x:hidden;line-height:1.75}

/* ─── NAV ─── */
.nav{position:sticky;top:0;z-index:100;background:rgba(248,246,241,0.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);padding:0.6rem 1rem;display:flex;align-items:center;gap:1rem;overflow-x:auto}
.nav-logo{font-family:'Outfit',sans-serif;font-weight:900;font-size:0.85rem;color:var(--api);white-space:nowrap}
.nav a{font-size:0.78rem;color:var(--dim);text-decoration:none;white-space:nowrap;transition:color 0.2s}
.nav a:hover{color:var(--api)}

/* ─── HERO ─── */
.hero{text-align:center;padding:5rem 2rem 3rem;background:linear-gradient(180deg,#f0ede6,var(--bg))}
.hero-badge{display:inline-block;padding:0.35rem 1rem;border:1.5px solid var(--api);border-radius:100px;font-size:0.75rem;color:var(--api);letter-spacing:2px;margin-bottom:1.5rem}
.hero h1{font-family:'Outfit',sans-serif;font-size:clamp(2rem,5vw,3.2rem);font-weight:900;line-height:1.3}
.hero h1 .hl{color:var(--api)}
.hero-sub{font-size:1.05rem;color:var(--dim);margin-top:0.8rem;max-width:600px;margin-left:auto;margin-right:auto}

/* ─── SECTIONS ─── */
.sec{max-width:900px;margin:0 auto;padding:4rem 1.5rem;scroll-margin-top:3.5rem}
.sec-label{display:inline-block;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;padding:0.25rem 0.7rem;border-radius:5px;margin-bottom:0.8rem}
.lb-concept{background:var(--api-bg);color:var(--api)}
.lb-key{background:rgba(245,158,11,0.1);color:var(--cl)}
.lb-yt{background:var(--yt-bg);color:var(--yt)}
.lb-cl{background:var(--cl-bg);color:var(--cl)}
.lb-code{background:var(--green-bg);color:var(--green)}
.lb-quiz{background:rgba(239,68,68,0.08);color:var(--red)}
.sec h2{font-family:'Outfit',sans-serif;font-size:1.8rem;font-weight:900;margin-bottom:0.5rem}
.sec .lead{color:var(--dim);font-size:0.95rem;margin-bottom:2rem;max-width:680px}

/* ─── CARDS ─── */
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1.8rem;margin-bottom:1.5rem;box-shadow:0 1px 4px rgba(0,0,0,0.03)}
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin:1.5rem 0}
.card-sm{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.3rem;text-align:center;transition:all 0.2s}
.card-sm:hover{border-color:var(--api);transform:translateY(-2px)}
.card-sm .icon{font-size:2rem;margin-bottom:0.5rem}
.card-sm h4{font-size:0.9rem;margin-bottom:0.3rem}
.card-sm .real{font-family:'IBM Plex Mono',monospace;font-size:0.7rem;color:var(--api);margin-bottom:0.4rem}
.card-sm p{font-size:0.78rem;color:var(--dim);line-height:1.5}

/* ─── CODE ─── */
.code{background:var(--code-bg);color:var(--code-text);border-radius:10px;padding:1.1rem 1.2rem;font-family:'IBM Plex Mono',monospace;font-size:0.73rem;line-height:1.85;overflow-x:auto;white-space:pre-wrap;margin:1rem 0;position:relative}
.copy-btn{position:absolute;top:0.6rem;right:0.6rem;background:rgba(255,255,255,0.08);color:#888;border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.65rem;cursor:pointer;font-family:'IBM Plex Mono',monospace;transition:all 0.2s;z-index:2}
.copy-btn:hover{background:rgba(255,255,255,0.15);color:#ccc}
.code-label{display:inline-block;background:var(--code-bg);color:#89b4fa;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;padding:0.2rem 0.6rem;border-radius:6px 6px 0 0;margin-bottom:-1px;position:relative;z-index:1}
.dk{color:#89b4fa}.ds{color:#a6e3a1}.dn{color:#fab387}.dc{color:#6c7086}.du{color:#cba6f7}.df{color:#f38ba8}

/* ─── MUST-KNOW ─── */
.mk{background:var(--card);border:1.5px solid var(--border);border-radius:18px;padding:2rem;margin:1.5rem 0}
.mk-badge{font-family:'IBM Plex Mono',monospace;font-size:0.62rem;padding:0.2rem 0.6rem;border-radius:5px;font-weight:700;letter-spacing:1px}
.mk-badge-key{background:rgba(245,158,11,0.12);color:var(--cl)}
.mk-badge-json{background:var(--api-bg);color:var(--api)}
.mk-title{font-family:'Outfit',sans-serif;font-size:1.2rem;font-weight:900;margin:0.5rem 0 0.8rem}
.mk p{font-size:0.9rem;color:var(--dim);line-height:1.8}
.mk strong{color:var(--text)}
.mk em{color:var(--cl);font-style:normal}

.analogy{background:rgba(245,158,11,0.04);border:1px solid rgba(245,158,11,0.15);border-radius:10px;padding:1rem 1.2rem;margin:1rem 0;font-size:0.85rem}
.dos-donts{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
.do-card,.dont-card{padding:0.8rem 1rem;border-radius:10px;font-size:0.8rem;line-height:1.7}
.do-card{background:var(--green-bg);border:1px solid rgba(16,185,129,0.2)}
.dont-card{background:rgba(239,68,68,0.04);border:1px solid rgba(239,68,68,0.15)}
.do-title{font-weight:700;font-size:0.75rem;margin-bottom:0.3rem}
.do-card .do-title{color:var(--green)}
.dont-card .do-title{color:var(--red)}

.json-compare{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
.json-col{background:var(--code-bg);border-radius:10px;padding:0.8rem 1rem;overflow-x:auto}
.json-col .jlabel{font-family:'IBM Plex Mono',monospace;font-size:0.62rem;padding:0.15rem 0.45rem;border-radius:4px;display:inline-block;margin-bottom:0.5rem}
.json-col pre{font-family:'IBM Plex Mono',monospace;font-size:0.72rem;line-height:1.8;color:var(--code-text);margin:0;white-space:pre-wrap}

/* ─── FOLD ─── */
.fold-toggle{display:flex;align-items:center;justify-content:space-between;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.3rem;cursor:pointer;transition:all 0.2s;margin:1.5rem 0 0}
.fold-toggle:hover{border-color:var(--api)}
.fold-toggle .ft-left{display:flex;align-items:center;gap:0.6rem}
.fold-toggle .ft-badge{background:var(--client-bg);color:var(--client);font-family:'IBM Plex Mono',monospace;font-size:0.6rem;padding:0.2rem 0.5rem;border-radius:5px;letter-spacing:1px;font-weight:600}
.fold-toggle .ft-title{font-weight:700;font-size:0.9rem}
.fold-toggle .ft-arrow{transition:transform 0.3s;color:var(--dim)}
.fold-toggle.open .ft-arrow{transform:rotate(90deg)}
.fold-body{display:none;padding-top:1rem}
.fold-body.open{display:block}

.term-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}
.term-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.2rem;transition:all 0.2s}
.term-card:hover{border-color:var(--client)}
.term-tag{display:inline-block;font-family:'IBM Plex Mono',monospace;font-size:0.6rem;padding:0.15rem 0.45rem;border-radius:4px;margin-bottom:0.6rem;font-weight:600}
.tag-get{background:var(--green-bg);color:var(--green)}
.tag-post{background:var(--client-bg);color:var(--client)}
.tag-key{background:rgba(245,158,11,0.1);color:var(--cl)}
.term-card h4{font-size:0.95rem;margin-bottom:0.4rem}
.term-card p{font-size:0.78rem;color:var(--dim);line-height:1.6}

/* ─── SEQUENCE DIAGRAM ─── */
.scene-box{background:var(--card);border:1.5px solid var(--border);border-radius:20px;padding:1.5rem;margin:2rem 0;overflow:hidden}
.stage{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.5rem;margin-bottom:0.8rem;padding:0.6rem 0;border-bottom:1px solid var(--border)}
.entity{text-align:center}
.entity-icon{font-size:2rem;margin-bottom:0.2rem}
.entity-name{font-family:'Outfit',sans-serif;font-weight:800;font-size:0.85rem;letter-spacing:0.5px}
.entity-sub{font-size:0.6rem;color:var(--dim);font-family:'IBM Plex Mono',monospace}
.entity.e-client .entity-name{color:var(--client)}
.entity.e-yt .entity-name{color:var(--yt)}
.entity.e-cl .entity-name{color:var(--cl)}

/* Entity activity indicator */
.entity{position:relative;transition:all 0.4s}
.e-indicator{
  display:inline-flex;align-items:center;gap:0.2rem;
  margin-top:0.3rem;height:22px;
  font-size:0.6rem;font-weight:700;
  padding:0.15rem 0.5rem;border-radius:100px;
  opacity:0;transform:scale(0.8);transition:all 0.4s;
}
.entity.active .e-indicator{opacity:1;transform:scale(1)}
.e-indicator.ei-client{background:var(--client-bg);color:var(--client);border:1px solid rgba(59,109,245,0.2)}
.e-indicator.ei-api{background:rgba(139,92,246,0.08);color:var(--api);border:1px solid rgba(139,92,246,0.2)}
.e-indicator.ei-yt{background:var(--yt-bg);color:var(--yt);border:1px solid rgba(227,51,51,0.2)}
.e-indicator.ei-cl{background:var(--cl-bg);color:var(--cl);border:1px solid rgba(217,119,6,0.2)}

.e-pulse{width:8px;height:8px;border-radius:50%;animation:pulse 1.2s ease-in-out infinite}
.ei-client .e-pulse{background:var(--client)}
.ei-yt .e-pulse{background:var(--yt)}
.ei-cl .e-pulse{background:var(--cl)}
.ei-api .e-pulse{background:var(--api)}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.4;transform:scale(0.7)}}
.entity.done .e-indicator{opacity:0.4}
.entity.done .e-pulse{animation:none}

/* Steps: hidden by default, shown one at a time */
.seq-step{
  display:none;
  grid-template-columns:1fr 1.2fr 1fr;
  gap:0;align-items:stretch;min-height:60px;
  min-width:0;
}
.seq-step>*{min-width:0}
.seq-step.current{display:grid;animation:fadeSlide 0.5s ease}

/* Timeline mode: show ALL steps stacked */
.scene-box.timeline .seq-step{display:grid !important;animation:none}
.scene-box.timeline .seq-step+.seq-step{border-top:1px dashed var(--border);padding-top:0.8rem;margin-top:0.5rem}

@keyframes fadeSlide{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

.step-line{display:flex;justify-content:center;position:relative}
.step-line::before{content:'';position:absolute;top:0;bottom:0;left:50%;width:2px;transform:translateX(-50%)}
.step-line.sl-c::before{background:rgba(59,109,245,0.12)}
.step-line.sl-yt::before{background:rgba(227,51,51,0.12)}
.step-line.sl-cl::before{background:rgba(217,119,6,0.12)}

.act-box{position:absolute;top:6px;bottom:6px;left:50%;transform:translateX(-50%);width:18px;border-radius:4px}
.act-box.ab-c{background:var(--client-bg);border:1px solid rgba(59,109,245,0.2)}
.act-box.ab-yt{background:var(--yt-bg);border:1px solid rgba(227,51,51,0.2)}
.act-box.ab-cl{background:var(--cl-bg);border:1px solid rgba(217,119,6,0.2)}

.arrow-area{display:flex;flex-direction:column;justify-content:center;gap:0.2rem;padding:0.4rem 0}

.step-info{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:0.6rem 0.8rem;font-size:0.78rem;color:var(--dim);line-height:1.55;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.03)}
.step-info strong{color:var(--text)}

.sbadge{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;font-family:'IBM Plex Mono',monospace;font-size:0.6rem;font-weight:700;color:white;margin-right:0.2rem;vertical-align:middle}
.sb-req{background:var(--client)}
.sb-res{background:var(--green)}
.sb-srv{background:var(--api)}

.arrow{display:flex;align-items:center;position:relative;margin-top:1.2rem}
.arrow-line{flex:1;height:2px;position:relative}
.arrow-line::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%}
.arrow.req .arrow-line::before{background:var(--client)}
.arrow.res .arrow-line::before{background:var(--green)}
.arrow-head{width:0;height:0;flex-shrink:0;border-top:5px solid transparent;border-bottom:5px solid transparent}
.arrow.req .arrow-head{border-left:8px solid var(--client)}
.arrow.res .arrow-head{border-right:8px solid var(--green)}
.arrow-tag{position:absolute;top:-20px;left:50%;transform:translateX(-50%);padding:0.15rem 0.5rem;border-radius:5px;font-family:'IBM Plex Mono',monospace;font-size:0.58rem;font-weight:600;white-space:nowrap}
.arrow.req .arrow-tag{background:var(--client-bg);color:var(--client);border:1px solid rgba(59,109,245,0.15)}
.arrow.res .arrow-tag{background:var(--green-bg);color:#059669;border:1px solid rgba(16,185,129,0.15)}

.detail{grid-column:1/-1;background:var(--code-bg);border-radius:10px;padding:0.8rem 1rem;margin:0.3rem 0 0.5rem;font-family:'IBM Plex Mono',monospace;font-size:0.68rem;line-height:1.8;color:var(--code-text);white-space:pre-wrap;overflow:hidden;word-break:break-word}

/* UI Mockup */
.ui-mock{grid-column:1/-1;max-width:480px;margin:0.5rem auto 1rem;background:#fff;border:1.5px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:0 3px 15px rgba(0,0,0,0.05)}
.ui-tb{background:#f5f5f8;border-bottom:1px solid var(--border);padding:0.4rem 0.7rem;display:flex;align-items:center;gap:0.3rem}
.ui-d{width:7px;height:7px;border-radius:50%}.ui-d.r{background:#ff5f57}.ui-d.y{background:#ffbd2e}.ui-d.g{background:#28ca41}
.ui-tb-url{flex:1;text-align:center;font-size:0.55rem;color:var(--dim);font-family:'IBM Plex Mono',monospace}
.ui-bd{padding:1rem 1.2rem}
.ui-title{font-family:'Outfit',sans-serif;font-weight:800;font-size:0.95rem;margin-bottom:0.7rem}
.ui-il{font-size:0.68rem;color:var(--dim);margin-bottom:0.2rem;font-weight:600}
.ui-inp{width:100%;padding:0.45rem 0.7rem;border:1.5px solid var(--client);border-radius:7px;font-size:0.8rem;background:#fff;color:var(--text);font-family:'Noto Sans KR',sans-serif}
.ui-btn{display:inline-block;padding:0.4rem 1.2rem;border-radius:7px;font-size:0.78rem;font-weight:700;border:none;margin-top:0.5rem;color:white}
.ui-btn-yt{background:var(--yt)}
.ui-btn-cl{background:var(--cl)}
.ui-spin{display:inline-flex;align-items:center;gap:0.4rem;font-size:0.75rem;color:var(--dim);margin-top:0.5rem}
.ui-spin-d{width:12px;height:12px;border:2px solid var(--border);border-top-color:var(--api);border-radius:50%;animation:spin 0.8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.ui-metrics{display:flex;gap:0.5rem;margin-bottom:0.6rem}
.ui-m{flex:1;background:#f7f7fa;border:1px solid var(--border);border-radius:7px;padding:0.4rem;text-align:center}
.ui-m-l{font-size:0.55rem;color:var(--dim)}.ui-m-v{font-family:'Outfit',sans-serif;font-weight:800;font-size:0.95rem}
.ui-bar-r{display:flex;align-items:center;gap:0.4rem;margin-bottom:0.3rem}
.ui-bar-l{font-size:0.62rem;width:100px;text-align:right;color:var(--dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ui-bar{height:16px;border-radius:3px}
.ui-bar-v{font-size:0.55rem;color:var(--dim);font-family:'IBM Plex Mono',monospace}
.ui-ai{background:#f0f7ff;border:1px solid #d0e3ff;border-radius:10px;padding:0.7rem 0.9rem;font-size:0.78rem;line-height:1.7;margin:0.5rem 0}
.ui-tok{display:flex;gap:0.8rem;font-size:0.6rem;color:var(--dim);font-family:'IBM Plex Mono',monospace;margin-top:0.4rem}

.ui-trans{grid-column:1/-1;text-align:center;padding:0.6rem 0}
.ui-trans-lbl{display:inline-block;background:var(--api-bg);border:1.5px dashed var(--api);border-radius:100px;padding:0.35rem 1rem;font-size:0.75rem;font-weight:700;color:var(--api)}

.scene-controls{display:flex;justify-content:center;gap:0.7rem;margin-top:1.5rem;align-items:center}
.sc-btn{padding:0.6rem 1.8rem;border-radius:100px;font-family:'Noto Sans KR',sans-serif;font-size:0.85rem;font-weight:700;cursor:pointer;border:none;transition:all 0.3s}
.sc-primary{background:var(--api);color:white;box-shadow:0 3px 12px rgba(139,92,246,0.2)}
.sc-primary:hover{transform:scale(1.05)}
.sc-secondary{background:var(--card);color:var(--dim);border:1.5px solid var(--border)}
.sc-counter{font-family:'IBM Plex Mono',monospace;font-size:0.78rem;color:var(--dim)}

/* ─── COMPARISON ─── */
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin:1.5rem 0}
.cmp-card{background:var(--card);border:1.5px solid var(--border);border-radius:14px;padding:1.5rem}
.cmp-card h4{font-size:0.95rem;font-weight:800;margin-bottom:0.7rem}
.cmp-card p{font-size:0.8rem;color:var(--dim);line-height:1.8}
.cmp-card strong{color:var(--text)}
.cmp-card code{font-family:'IBM Plex Mono',monospace;font-size:0.68rem;background:#f0f0f5;padding:0.1rem 0.3rem;border-radius:3px}

/* ─── QUIZ ─── */
.quiz-box{background:var(--card);border:1.5px solid var(--border);border-radius:18px;padding:2rem}
.quiz-q{font-size:1.05rem;font-weight:700;margin-bottom:1.2rem}
.quiz-opts{display:flex;flex-direction:column;gap:0.6rem}
.quiz-opt{background:var(--bg);border:2px solid var(--border);border-radius:10px;padding:0.8rem 1.2rem;cursor:pointer;font-size:0.88rem;transition:all 0.3s}
.quiz-opt:hover{border-color:var(--api)}
.quiz-opt.correct{border-color:var(--green);background:var(--green-bg)}
.quiz-opt.wrong{border-color:var(--red);background:rgba(239,68,68,0.04)}
.quiz-fb{margin-top:1rem;padding:0.8rem 1rem;border-radius:10px;font-size:0.88rem;display:none}
.quiz-nav{display:flex;justify-content:space-between;align-items:center;margin-top:1.5rem}
.quiz-score{font-family:'IBM Plex Mono',monospace;font-size:0.8rem;color:var(--api)}

/* ─── FOOTER ─── */
.footer{text-align:center;padding:3rem 2rem;border-top:1px solid var(--border);color:var(--dim);font-size:0.78rem}

/* ─── RESTAURANT 3-COLUMN ─── */
.resto{position:relative}
.resto3{display:flex;flex-direction:column;gap:0}

.r3-header{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.6rem;margin-bottom:0.8rem}
.r3-h{text-align:center;padding:0.6rem;border-radius:10px;font-weight:800;font-size:0.82rem}
.r3-hsub{font-size:0.6rem;font-weight:400;color:inherit;opacity:0.7;margin-top:0.1rem}
.r3-h-client{background:var(--client-bg);color:var(--client)}
.r3-h-api{background:rgba(245,158,11,0.08);color:#b45309}
.r3-h-server{background:var(--green-bg);color:#047857}

.r3-row{display:grid;grid-template-columns:1fr 0.8fr 1fr;gap:0.6rem;margin-bottom:0.6rem}

.r3-cell{padding:0.8rem;border-radius:12px;font-size:0.78rem;line-height:1.6;text-align:center}
.r3-client{background:#fafafe;border:1.5px solid rgba(59,109,245,0.12)}
.r3-api{background:#fffbf0;border:1.5px solid rgba(245,158,11,0.15);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.15rem}
.r3-server{background:#f7fdf9;border:1.5px solid rgba(16,185,129,0.12)}

.r3-emoji{font-size:1.6rem;margin-bottom:0.2rem}
.r3-title{font-weight:800;font-size:0.82rem;color:var(--text);margin-bottom:0.15rem}
.r3-desc{font-size:0.75rem;color:var(--dim);margin-bottom:0.3rem}
.r3-real{font-size:0.68rem;color:var(--api);background:var(--api-bg);padding:0.2rem 0.5rem;border-radius:5px;display:inline-block}

.r3-num{width:26px;height:26px;border-radius:50%;background:#f59e0b;color:white;display:flex;align-items:center;justify-content:center;font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:700}
.r3-arrow-d{font-size:1.1rem;color:#d97706;font-weight:800;line-height:1}
.r3-api-action{font-weight:700;font-size:0.78rem;color:#92400e}
.r3-api .r3-real{background:rgba(245,158,11,0.08);color:#92400e}

/* ─── THUMBNAILS ─── */
.yt-result{border-top:1px solid var(--border);padding-top:0.5rem;margin-top:0.3rem}
.yt-row{display:flex;align-items:center;gap:0.6rem;padding:0.4rem 0;border-bottom:1px solid #f0f0f5}
.yt-row:last-child{border-bottom:none}
.yt-thumb{width:64px;height:36px;border-radius:5px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:1.2rem;position:relative;overflow:hidden}
.yt-thumb img{width:100%;height:100%;object-fit:cover;border-radius:5px}
.yt-info{flex:1;min-width:0}
.yt-info-title{font-size:0.7rem;font-weight:700;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.yt-info-ch{font-size:0.58rem;color:var(--dim)}
.yt-views{font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:var(--yt);font-weight:600;white-space:nowrap}

/* ─── RESPONSIVE ─── */
@media(max-width:768px){
  .stage,.seq-step{grid-template-columns:60px 1fr 60px}
  .entity-icon{font-size:1.4rem}.entity-name{font-size:0.65rem}.entity-sub{font-size:0.5rem}
  .scene-box{padding:1rem 0.8rem}
  .detail{font-size:0.58rem;padding:0.6rem}
  .arrow-tag{font-size:0.5rem}
  .step-info{font-size:0.68rem;padding:0.4rem 0.5rem}
  .dos-donts,.json-compare,.cmp{grid-template-columns:1fr}
  .resto-step{grid-template-columns:1fr 30px 1fr}
  .resto-left,.resto-right{padding:0.5rem 0.6rem;font-size:0.72rem}
  .r3-header,.r3-row{grid-template-columns:1fr}
  .r3-row{gap:0.4rem;margin-bottom:1rem}
  .r3-api{flex-direction:row;gap:0.5rem;padding:0.5rem}
  .r3-cell{padding:0.6rem}
  .yt-thumb{width:48px;height:27px;font-size:0.9rem}
  .card-grid{grid-template-columns:1fr 1fr}
  .scene-box{padding:1.2rem 0.8rem}
  .detail{margin:0.3rem 0 0.5rem;font-size:0.6rem}
  .sec{padding:3rem 1rem}
}
</style>
</head>
<body>

<!-- NAV -->
<div class="nav">
  <div class="nav-logo">🔌 API 특강</div>
  <a href="#concept">개념</a>
  <a href="#musthave">핵심용어</a>
  <a href="#flow-yt">YouTube 흐름</a>
  <a href="#flow-cl">Claude 흐름</a>
  <a href="#code">바이브코딩</a>
  <a href="#quiz">퀴즈</a>
</div>

<!-- HERO -->
<section class="hero">
  <div class="hero-badge">SPECIAL LECTURE</div>
  <h1>석리송 선생님의<br><span class="hl">API</span> 특강!</h1>
  <p class="hero-sub">API가 뭔지, 어떻게 작동하는지, 직접 코드로 써보는 것까지.<br>이 페이지 하나로 전부 배워봅시다.</p>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 1: API 개념                        -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="concept">
  <span class="sec-label lb-concept">SECTION 01</span>
  <h2>API가 뭔데?</h2>
  <p class="lead">API(Application Programming Interface)는 <strong>프로그램끼리 대화하는 규칙</strong>입니다. 예약제 레스토랑에 비유하면 아주 쉽게 이해할 수 있어요.</p>

  <div class="card resto">
    <h3 style="font-size:1.1rem;margin-bottom:0.3rem">🍽️ 예약제 레스토랑으로 이해하는 API</h3>
    <p style="font-size:0.82rem;color:var(--dim);margin-bottom:1.2rem">왼쪽은 <strong>손님(내 앱)</strong>, 가운데는 <strong>웨이터(API)</strong>, 오른쪽은 <strong>주방(서버)</strong>입니다.</p>

    <div class="resto3">
      <!-- Header -->
      <div class="r3-header">
        <div class="r3-h r3-h-client">🧑‍💻 손님 (내 앱)<div class="r3-hsub">Client</div></div>
        <div class="r3-h r3-h-api">🤵 웨이터 (API)<div class="r3-hsub">중간 전달자</div></div>
        <div class="r3-h r3-h-server">👨‍🍳 주방 (서버)<div class="r3-hsub">YouTube / Claude</div></div>
      </div>

      <!-- Step 1 -->
      <div class="r3-row">
        <div class="r3-cell r3-client">
          <div class="r3-emoji">🚪🧑</div>
          <div class="r3-title">예약제 레스토랑에 들어감</div>
          <div class="r3-desc">"안녕하세요, 예약한 사람인데요"</div>
          <div class="r3-real">내 앱이 API 키를 들고 접속</div>
        </div>
        <div class="r3-cell r3-api">
          <div class="r3-num">1</div>
          <div class="r3-arrow-d">→</div>
          <div class="r3-api-action">예약 번호 확인</div>
          <div class="r3-real">API 키가 유효한지 인증</div>
        </div>
        <div class="r3-cell r3-server">
          <div class="r3-emoji">🔑✅</div>
          <div class="r3-title">예약 확인 완료</div>
          <div class="r3-desc">"네, 확인됐습니다. 들어오세요!"</div>
          <div class="r3-real">서버가 API 키를 승인</div>
        </div>
      </div>

      <!-- Step 2 -->
      <div class="r3-row">
        <div class="r3-cell r3-client">
          <div class="r3-emoji">📋👀</div>
          <div class="r3-title">메뉴판을 봄</div>
          <div class="r3-desc">"여기 뭘 시킬 수 있지?"</div>
          <div class="r3-real">API 문서를 읽어봄</div>
        </div>
        <div class="r3-cell r3-api">
          <div class="r3-num">2</div>
          <div class="r3-api-action">메뉴판 제공</div>
          <div class="r3-real" style="text-align:left;font-size:0.68rem">
            📺 영상 검색<br>
            👁️ 조회수 조회<br>
            💬 댓글 조회<br>
            👍 좋아요 수 조회
          </div>
        </div>
        <div class="r3-cell r3-server">
          <div class="r3-emoji">📊</div>
          <div class="r3-title">제공 가능한 데이터 보유</div>
          <div class="r3-desc">수십억 개의 영상 정보가 저장되어 있음</div>
          <div class="r3-real">YouTube 데이터베이스</div>
        </div>
      </div>

      <!-- Step 3 -->
      <div class="r3-row">
        <div class="r3-cell r3-client">
          <div class="r3-emoji">🗣️</div>
          <div class="r3-title">웨이터에게 주문!</div>
          <div class="r3-desc">"귀여운 고양이 영상 5개 주세요!"</div>
          <div class="r3-real"><code style="font-size:0.63rem">q=귀여운 고양이&maxResults=5</code></div>
        </div>
        <div class="r3-cell r3-api">
          <div class="r3-num">3</div>
          <div class="r3-arrow-d">→</div>
          <div class="r3-api-action">주문을 주방에 전달</div>
          <div class="r3-real">GET 요청을 서버로 전송</div>
        </div>
        <div class="r3-cell r3-server">
          <div class="r3-emoji">👨‍🍳🔥</div>
          <div class="r3-title">주문 접수, 요리 시작!</div>
          <div class="r3-desc">셰프가 주문에 맞는 음식을 만들기 시작</div>
          <div class="r3-real">서버가 데이터를 검색·정렬</div>
        </div>
      </div>

      <!-- Step 4 -->
      <div class="r3-row">
        <div class="r3-cell r3-client">
          <div class="r3-emoji">😋🍝</div>
          <div class="r3-title">음식을 받음!</div>
          <div class="r3-desc">"맛있겠다~ 먹어볼까?"</div>
          <div class="r3-real">JSON 데이터를 받아서 화면에 표시</div>
        </div>
        <div class="r3-cell r3-api">
          <div class="r3-num">4</div>
          <div class="r3-arrow-d">←</div>
          <div class="r3-api-action">음식을 테이블로 서빙</div>
          <div class="r3-real"><code style="font-size:0.63rem;color:var(--green)">200 OK + JSON</code></div>
        </div>
        <div class="r3-cell r3-server">
          <div class="r3-emoji">📦✨</div>
          <div class="r3-title">요리 완성, 포장!</div>
          <div class="r3-desc">접시에 예쁘게 담아서 내보냄</div>
          <div class="r3-real">결과를 JSON 형식으로 포장해 전송</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 2: 핵심 개념 - API Key & JSON      -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="musthave">
  <span class="sec-label lb-key">SECTION 02</span>
  <h2>반드시 알아야 할 2가지</h2>
  <p class="lead">API를 쓸 때 가장 중요한 두 개념: <strong>API 키</strong>와 <strong>JSON</strong>.</p>

  <!-- API Key -->
  <div class="mk">
    <span class="mk-badge mk-badge-key">MUST KNOW</span>
    <div class="mk-title">🔑 API 키 (API Key)</div>
    <p><strong>서비스를 이용하기 위한 나만의 고유 비밀번호</strong>입니다. 서버가 <em>"이 요청은 허가된 사용자로부터 왔다"</em>고 확인하는 수단이에요.</p>
    <div class="analogy" style="background:rgba(239,68,68,0.04);border-color:rgba(239,68,68,0.2)">🚨 <strong>API 키가 유출되면?</strong> 다른 사람이 여러분의 키로 수만 번 요청을 보낼 수 있고, 그 비용이 전부 여러분에게 청구됩니다. 실제로 키 유출로 <em>수백만 원의 요금 폭탄</em>을 맞은 사례도 있어요. API 키는 비밀번호처럼 철저히 관리하세요!</div>
    <div class="dos-donts">
      <div class="do-card"><div class="do-title">✅ 이렇게 하세요</div>• Streamlit Secrets에 저장<br>• .env 파일 + .gitignore<br>• 환경변수로 관리</div>
      <div class="dont-card"><div class="do-title">❌ 절대 하면 안 되는 것</div>• 코드에 직접 적기<br>• 카톡/메일로 공유<br>• GitHub에 올리기</div>
    </div>
    <div class="code">
<span class="dc"># ✅ 올바른 방법</span>
API_KEY = st.secrets[<span class="ds">"YOUTUBE_API_KEY"</span>]

<span class="dc"># ❌ 잘못된 방법</span>
<span style="text-decoration:line-through;opacity:0.4">API_KEY = "AIzaSyD...실제키..."</span></div>
  </div>

  <!-- JSON -->
  <div class="mk">
    <span class="mk-badge mk-badge-json">MUST KNOW</span>
    <div class="mk-title">📋 JSON (제이슨)</div>
    <p><strong>API가 데이터를 주고받을 때 쓰는 표준 형식</strong>입니다. 핵심: <strong>중괄호 { } 안에 "이름": "값" 쌍</strong>. 파이썬 딕셔너리(dict)와 거의 동일!</p>
    <div class="json-compare">
      <div class="json-col"><div class="jlabel" style="background:var(--api-bg);color:var(--api)">JSON (API 응답)</div><pre>{
  <span class="dk">"title"</span>: <span class="ds">"파이썬 강좌"</span>,
  <span class="dk">"views"</span>: <span class="dn">152340</span>,
  <span class="dk">"tags"</span>: [<span class="ds">"파이썬"</span>, <span class="ds">"코딩"</span>]
}</pre></div>
      <div class="json-col"><div class="jlabel" style="background:var(--client-bg);color:var(--client)">Python (사용법)</div><pre>data = response.<span class="df">json</span>()

title = data[<span class="ds">"title"</span>]
views = data[<span class="ds">"views"</span>]
tag = data[<span class="ds">"tags"</span>][<span class="dn">0</span>]</pre></div>
    </div>
    <div class="analogy">📦 <strong>비유:</strong> JSON은 택배 박스의 송장(라벨)과 같아요. "보내는 사람": "홍길동", "무게": 2.5 이런 식으로 내용물을 정리해놓은 것!</div>
    <div class="code">
<span class="dc">// ⚠️ YouTube API는 조회수를 문자열로 줍니다!</span>
<span class="dk">"viewCount"</span>: <span class="ds">"152340"</span>   <span class="dc">← 숫자가 아니라 문자열!</span>

<span class="dc"># 반드시 int()로 변환!</span>
views = <span class="df">int</span>(data[<span class="ds">"viewCount"</span>])  <span class="dc">← 이제 숫자 152340</span></div>
  </div>

  <!-- Nice to know -->
  <div class="fold-toggle" id="fold-terms" onclick="this.classList.toggle('open');document.getElementById('fold-terms-body').classList.toggle('open')">
    <div class="ft-left"><span class="ft-badge">NICE TO KNOW</span><span class="ft-title">📚 더 알면 좋은 API 용어들</span></div>
    <span class="ft-arrow">▶</span>
  </div>
  <div class="fold-body" id="fold-terms-body">
    <div class="term-grid">
      <div class="term-card"><span class="term-tag tag-get">METHOD</span><h4>HTTP 메서드</h4><p><strong>GET</strong> — 데이터 가져오기<br><strong>POST</strong> — 데이터 보내기<br>우리 수업에서는 대부분 GET만 사용!</p></div>
      <div class="term-card"><span class="term-tag tag-post">ENDPOINT</span><h4>엔드포인트</h4><p>API 기능별 URL 주소.<br><code style="color:var(--api)">/search</code> → 검색<br><code style="color:var(--api)">/videos</code> → 영상 정보</p></div>
      <div class="term-card"><span class="term-tag tag-get">STATUS</span><h4>상태 코드</h4><p><strong>200</strong> — 성공! ✅<br><strong>401</strong> — API 키 오류 🔑<br><strong>404</strong> — 못 찾겠음 🔍<br><strong>429</strong> — 너무 많이 요청 ⏳</p></div>
      <div class="term-card"><span class="term-tag tag-key">QUOTA</span><h4>요청 제한 (쿼터)</h4><p>YouTube API: 하루 <strong>10,000 쿼터</strong> 무료<br>검색 1회 = 100 쿼터<br>→ 하루 최대 약 100회 검색</p></div>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 3: YouTube API 흐름                -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="flow-yt">
  <span class="sec-label lb-yt">SECTION 03</span>
  <h2>▶ YouTube API는 이렇게 작동합니다</h2>
  <p class="lead">"귀여운 고양이"를 검색하면, 화면 뒤에서 무슨 일이 벌어지는지 한 단계씩 따라가 보세요.</p>

  <div class="scene-box">
    <div class="stage">
      <div class="entity e-client" id="yt-ec"><div class="entity-icon">💻</div><div class="entity-name">CLIENT</div><div class="entity-sub">내 Streamlit 앱</div><div class="e-indicator ei-client"><div class="e-pulse"></div>작업 중</div></div>
      <div class="entity" id="yt-ea" style="display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:1.3rem">☁️</div><div style="font-family:'Outfit',sans-serif;font-weight:800;font-size:0.75rem;color:var(--api)">API</div><div class="e-indicator ei-api"><div class="e-pulse"></div>전달 중</div></div>
      <div class="entity e-yt" id="yt-es"><div class="entity-icon">🖥️</div><div class="entity-name">SERVER</div><div class="entity-sub">YouTube (Google)</div><div class="e-indicator ei-yt"><div class="e-pulse"></div>처리 중</div></div>
    </div>

    <!-- YT Step 0: UI Before -->
    <div class="seq-step" data-scene="yt" data-who="c">
      <div class="ui-mock">
        <div class="ui-tb"><div class="ui-d r"></div><div class="ui-d y"></div><div class="ui-d g"></div><div class="ui-tb-url">myapp.streamlit.app</div></div>
        <div class="ui-bd">
          <div class="ui-title">📺 YouTube 인기 영상 분석</div>
          <div class="ui-il">검색어를 입력하세요</div>
          <input class="ui-inp" value="귀여운 고양이" readonly>
          <div><span class="ui-btn ui-btn-yt">🔍 검색하기</span></div>
          <div class="ui-spin"><div class="ui-spin-d"></div>데이터를 가져오는 중...</div>
        </div>
      </div>
      <div class="ui-trans"><div class="ui-trans-lbl">⬇ 우리가 만든 웹앱을 실행할 때, 보이지 않는 곳에서 API를 통해 이런 일이 벌어집니다 ⬇</div></div>
    </div>

    <!-- YT Step 1 -->
    <div class="seq-step" data-scene="yt" data-who="c,a">
      <div class="step-line sl-c"><div class="act-box ab-c"></div></div>
      <div class="arrow-area">
        <div class="step-info"><span class="sbadge sb-req">1</span> <strong>GET 요청 전송</strong><br>"귀여운 고양이" 검색어 + API 키를 서버로 보냄</div>
        <div class="arrow req"><div class="arrow-line"></div><div class="arrow-head"></div><div class="arrow-tag">GET + API Key + 검색어</div></div>
      </div>
      <div class="step-line sl-yt"></div>
      <div class="detail">
<span class="dc"># 파이썬 코드</span>
response = requests.<span class="df">get</span>(
    <span class="ds">"https://www.googleapis.com/youtube/v3/search"</span>,
    params={<span class="dk">"q"</span>: <span class="ds">"귀여운 고양이"</span>, <span class="dk">"type"</span>: <span class="ds">"video"</span>, <span class="dk">"maxResults"</span>: <span class="dn">5</span>, <span class="dk">"key"</span>: <span class="ds">"AIzaSy..."</span>}
)</div>
    </div>

    <!-- YT Step 2 -->
    <div class="seq-step" data-scene="yt" data-who="s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-srv">2</span> <strong>서버: API 키 인증</strong><br>🔑 "이 키 유효한가?" → ✅ 확인 완료</div></div>
      <div class="step-line sl-yt"><div class="act-box ab-yt"></div></div>
    </div>

    <!-- YT Step 3 -->
    <div class="seq-step" data-scene="yt" data-who="s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-srv">3</span> <strong>서버: 데이터 검색</strong><br>⚙️ DB에서 "귀여운 고양이" 관련 영상 5개를 찾아 정렬</div></div>
      <div class="step-line sl-yt"><div class="act-box ab-yt"></div></div>
    </div>

    <!-- YT Step 4 -->
    <div class="seq-step" data-scene="yt" data-who="a,s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area">
        <div class="step-info"><span class="sbadge sb-res">4</span> <strong>JSON 응답 반환</strong><br>📦 결과를 JSON으로 포장하여 돌려보냄</div>
        <div class="arrow res"><div class="arrow-head"></div><div class="arrow-line"></div><div class="arrow-tag">200 OK (성공!) + JSON</div></div>
      </div>
      <div class="step-line sl-yt"><div class="act-box ab-yt"></div></div>
      <div class="detail">
<span class="dc">// 서버 → 내 앱으로 전송되는 JSON</span>
{
  <span class="dk">"items"</span>: [{
    <span class="dk">"snippet"</span>: {
      <span class="dk">"title"</span>: <span class="ds">"고양이가 상자에 들어가는 영상 모음"</span>,
      <span class="dk">"channelTitle"</span>: <span class="ds">"크림히어로즈"</span>
    },
    <span class="dk">"statistics"</span>: {
      <span class="dk">"viewCount"</span>: <span class="ds">"52341876"</span>  <span class="dc">← ⚠️ 문자열! int() 필요</span>
    }
  }, ...]
}</div>
    </div>

    <!-- YT Step 5 -->
    <div class="seq-step" data-scene="yt" data-who="c">
      <div class="step-line sl-c"><div class="act-box ab-c"></div></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-req">5</span> <strong>데이터 파싱 & 화면 표시</strong><br>📊 JSON에서 필요한 정보를 꺼내서 차트/표로 표시</div></div>
      <div class="step-line sl-yt"></div>
    </div>

    <!-- YT Step 6: UI Result -->
    <div class="seq-step" data-scene="yt" data-who="c">
      <div class="ui-trans"><div class="ui-trans-lbl">⬆ 위 과정이 끝나면, 화면에 결과가 나타납니다 ⬆</div></div>
      <div class="ui-mock">
        <div class="ui-tb"><div class="ui-d r"></div><div class="ui-d y"></div><div class="ui-d g"></div><div class="ui-tb-url">myapp.streamlit.app</div></div>
        <div class="ui-bd">
          <div class="ui-title">📺 YouTube 인기 영상 분석</div>
          <div class="ui-metrics">
            <div class="ui-m"><div class="ui-m-l">검색 결과</div><div class="ui-m-v">5건</div></div>
            <div class="ui-m"><div class="ui-m-l">평균 조회수</div><div class="ui-m-v">3,740만</div></div>
            <div class="ui-m"><div class="ui-m-l">평균 좋아요</div><div class="ui-m-v">89만</div></div>
          </div>
          <div style="font-size:0.72rem;font-weight:700;margin-bottom:0.3rem">🏆 조회수 TOP 3</div>
          <div class="yt-result">
            <div class="yt-row">
              <div class="yt-thumb" style="background:linear-gradient(135deg,#ffe4cc,#ffd1a8)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/220px-Cat_November_2010-1a.jpg" onerror="this.style.display='none';this.parentElement.textContent='🐱📦'"></div>
              <div class="yt-info"><div class="yt-info-title">고양이가 상자에 들어가는 영상 모음</div><div class="yt-info-ch">크림히어로즈 · 조회수</div></div>
              <div class="yt-views">5,234만</div>
            </div>
            <div class="yt-row">
              <div class="yt-thumb" style="background:linear-gradient(135deg,#e8d5f5,#d4b8e8)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/220px-Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg" onerror="this.style.display='none';this.parentElement.textContent='🐱✋'"></div>
              <div class="yt-info"><div class="yt-info-title">냥이 꾹꾹이 ASMR 30분</div><div class="yt-info-ch">고양이 왕국 · 조회수</div></div>
              <div class="yt-views">3,120만</div>
            </div>
            <div class="yt-row">
              <div class="yt-thumb" style="background:linear-gradient(135deg,#d1ecf1,#b8dce3)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on_snow.jpg/220px-Felis_catus-cat_on_snow.jpg" onerror="this.style.display='none';this.parentElement.textContent='🐱🌿'"></div>
              <div class="yt-info"><div class="yt-info-title">아기 고양이 첫 산책 브이로그</div><div class="yt-info-ch">냥집사 일기 · 조회수</div></div>
              <div class="yt-views">2,870만</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="scene-controls">
      <button class="sc-btn sc-secondary" onclick="resetScene('yt')">처음으로</button>
      <button class="sc-btn sc-secondary" onclick="prevStep('yt')">← 이전</button>
      <span class="sc-counter" id="cnt-yt">0 / 7</span>
      <button class="sc-btn sc-primary" id="btn-yt" onclick="nextStep('yt')">다음 단계 →</button>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 4: Claude API 흐름                 -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="flow-cl">
  <span class="sec-label lb-cl">SECTION 04</span>
  <h2>🤖 Claude API는 이렇게 작동합니다</h2>
  <p class="lead">AI에게 질문을 던지면, 화면 뒤에서 무슨 일이 벌어지는지 확인해보세요.</p>

  <div class="scene-box">
    <div class="stage">
      <div class="entity e-client" id="cl-ec"><div class="entity-icon">💻</div><div class="entity-name">CLIENT</div><div class="entity-sub">내 Streamlit 앱</div><div class="e-indicator ei-client"><div class="e-pulse"></div>작업 중</div></div>
      <div class="entity" id="cl-ea" style="display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:1.3rem">☁️</div><div style="font-family:'Outfit',sans-serif;font-weight:800;font-size:0.75rem;color:var(--api)">API</div><div class="e-indicator ei-api"><div class="e-pulse"></div>전달 중</div></div>
      <div class="entity e-cl" id="cl-es"><div class="entity-icon">🖥️</div><div class="entity-name">SERVER</div><div class="entity-sub">Anthropic (Claude)</div><div class="e-indicator ei-cl"><div class="e-pulse"></div>처리 중</div></div>
    </div>

    <!-- CL Step 0: UI Before -->
    <div class="seq-step" data-scene="cl" data-who="c">
      <div class="ui-mock">
        <div class="ui-tb"><div class="ui-d r"></div><div class="ui-d y"></div><div class="ui-d g"></div><div class="ui-tb-url">myapp.streamlit.app</div></div>
        <div class="ui-bd">
          <div class="ui-title">🤖 AI 질문 도우미</div>
          <div class="ui-il">궁금한 것을 질문해보세요</div>
          <input class="ui-inp" value="API가 뭐야? 중학생에게 설명해줘" readonly style="font-size:0.75rem">
          <div><span class="ui-btn ui-btn-cl">🚀 질문하기</span></div>
          <div class="ui-spin"><div class="ui-spin-d"></div>AI가 생각하는 중...</div>
        </div>
      </div>
      <div class="ui-trans"><div class="ui-trans-lbl">⬇ 우리가 만든 웹앱을 실행할 때, 보이지 않는 곳에서 API를 통해 이런 일이 벌어집니다 ⬇</div></div>
    </div>

    <!-- CL Step 1 -->
    <div class="seq-step" data-scene="cl" data-who="c,a">
      <div class="step-line sl-c"><div class="act-box ab-c"></div></div>
      <div class="arrow-area">
        <div class="step-info"><span class="sbadge sb-req">1</span> <strong>POST 요청 전송</strong><br>"API가 뭐야?" 질문 + API 키를 서버로 보냄</div>
        <div class="arrow req"><div class="arrow-line"></div><div class="arrow-head"></div><div class="arrow-tag">POST + API Key + 메시지</div></div>
      </div>
      <div class="step-line sl-cl"></div>
      <div class="detail">
<span class="dc"># 파이썬 코드</span>
<span class="du">import</span> anthropic
client = anthropic.<span class="df">Anthropic</span>(api_key=<span class="ds">"sk-ant-..."</span>)
message = client.messages.<span class="df">create</span>(
    model=<span class="ds">"claude-sonnet-4-6"</span>, max_tokens=<span class="dn">1024</span>,
    messages=[{<span class="dk">"role"</span>: <span class="ds">"user"</span>, <span class="dk">"content"</span>: <span class="ds">"API가 뭐야? 중학생에게 설명해줘"</span>}]
)</div>
    </div>

    <!-- CL Step 2 -->
    <div class="seq-step" data-scene="cl" data-who="s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-srv">2</span> <strong>서버: 인증 & 크레딧 확인</strong><br>🔑 키 유효? ✅ → 💰 잔액 충분? ✅</div></div>
      <div class="step-line sl-cl"><div class="act-box ab-cl"></div></div>
    </div>

    <!-- CL Step 3 -->
    <div class="seq-step" data-scene="cl" data-who="s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-srv">3</span> <strong>서버: AI 모델이 답변 생성</strong><br>🧠 Claude가 질문을 이해하고 토큰 단위로 답변 생성</div></div>
      <div class="step-line sl-cl"><div class="act-box ab-cl"></div></div>
    </div>

    <!-- CL Step 4 -->
    <div class="seq-step" data-scene="cl" data-who="a,s">
      <div class="step-line sl-c"></div>
      <div class="arrow-area">
        <div class="step-info"><span class="sbadge sb-res">4</span> <strong>JSON 응답 반환</strong><br>📦 AI 답변 + 토큰 사용량을 JSON으로 돌려보냄</div>
        <div class="arrow res"><div class="arrow-head"></div><div class="arrow-line"></div><div class="arrow-tag">200 OK (성공!) + JSON</div></div>
      </div>
      <div class="step-line sl-cl"><div class="act-box ab-cl"></div></div>
      <div class="detail">
<span class="dc">// Claude 서버 → 내 앱으로 전송되는 JSON</span>
{
  <span class="dk">"content"</span>: [{
    <span class="dk">"type"</span>: <span class="ds">"text"</span>,
    <span class="dk">"text"</span>: <span class="ds">"API는 프로그램끼리 대화하는 방법이에요! ..."</span>
  }],
  <span class="dk">"usage"</span>: {
    <span class="dk">"input_tokens"</span>: <span class="dn">24</span>,   <span class="dc">← 내 질문 길이</span>
    <span class="dk">"output_tokens"</span>: <span class="dn">67</span>   <span class="dc">← AI 답변 길이 (비용 발생)</span>
  }
}</div>
    </div>

    <!-- CL Step 5 -->
    <div class="seq-step" data-scene="cl" data-who="c">
      <div class="step-line sl-c"><div class="act-box ab-c"></div></div>
      <div class="arrow-area"><div class="step-info"><span class="sbadge sb-req">5</span> <strong>답변 추출 & 화면 표시</strong><br>📝 JSON에서 텍스트만 꺼내 화면에 표시</div></div>
      <div class="step-line sl-cl"></div>
    </div>

    <!-- CL Step 6: UI Result -->
    <div class="seq-step" data-scene="cl" data-who="c">
      <div class="ui-trans"><div class="ui-trans-lbl">⬆ 위 과정이 끝나면, 화면에 결과가 나타납니다 ⬆</div></div>
      <div class="ui-mock">
        <div class="ui-tb"><div class="ui-d r"></div><div class="ui-d y"></div><div class="ui-d g"></div><div class="ui-tb-url">myapp.streamlit.app</div></div>
        <div class="ui-bd">
          <div class="ui-title">🤖 AI 질문 도우미</div>
          <div style="font-size:0.75rem;font-weight:700;margin-bottom:0.3rem">💡 AI 답변</div>
          <div class="ui-ai">API는 프로그램끼리 대화하는 방법이에요! 마치 레스토랑에서 웨이터에게 주문하는 것처럼, 내 앱이 다른 서비스에게 "이것 좀 해줘!"라고 요청하는 거죠.</div>
          <div class="ui-tok"><span>📥 입력: 24 토큰</span><span>📤 출력: 67 토큰</span></div>
        </div>
      </div>
    </div>

    <div class="scene-controls">
      <button class="sc-btn sc-secondary" onclick="resetScene('cl')">처음으로</button>
      <button class="sc-btn sc-secondary" onclick="prevStep('cl')">← 이전</button>
      <span class="sc-counter" id="cnt-cl">0 / 7</span>
      <button class="sc-btn sc-primary" id="btn-cl" onclick="nextStep('cl')">다음 단계 →</button>
    </div>
  </div>

  <!-- Comparison -->
  <div class="cmp">
    <div class="cmp-card" style="border-color:rgba(227,51,51,0.2)">
      <h4 style="color:var(--yt)">▶ YouTube Data API</h4>
      <p><strong>요청:</strong> <code>GET</code> (데이터를 가져옴)<br><strong>응답:</strong> 이미 있는 영상 정보<br><strong>비용:</strong> 하루 10,000 쿼터 무료<br><strong>핵심:</strong> 기존 데이터를 <strong>조회</strong></p>
    </div>
    <div class="cmp-card" style="border-color:rgba(217,119,6,0.2)">
      <h4 style="color:var(--cl)">🤖 Claude API</h4>
      <p><strong>요청:</strong> <code>POST</code> (데이터를 보냄)<br><strong>응답:</strong> AI가 새로 만든 텍스트<br><strong>비용:</strong> 토큰당 종량제 (가입 시 ~$5)<br><strong>핵심:</strong> 새 콘텐츠를 <strong>생성</strong></p>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 5: 바이브 코딩 프롬프트             -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="code">
  <span class="sec-label lb-code">SECTION 05</span>
  <h2>바이브 코딩으로 만들기</h2>
  <p class="lead">코드를 직접 짤 필요 없어요. Claude에게 이렇게 말하면 됩니다!</p>

  <!-- YouTube Prompt -->
  <div class="card" style="border-left:4px solid var(--yt)">
    <h3 style="font-size:1rem;margin-bottom:0.5rem">📺 YouTube 앱 — 프롬프트 예시</h3>
    <p style="font-size:0.78rem;color:var(--dim);margin-bottom:0.8rem">💬 이렇게 Claude에게 말해보세요:</p>
    <div class="code" id="prompt-yt" style="background:#fef9f0;color:#92400e;border:2px solid var(--yt);font-size:0.82rem;line-height:2"><button class="copy-btn" onclick="copyPrompt('prompt-yt')">📋 복사</button>Streamlit Cloud에 배포할 웹앱을 만들어줘.

검색어를 입력하면 YouTube에서 영상을 검색해서
제목, 채널 이름, 조회수, 좋아요 수를 표로 보여주고,
조회수 순위 차트도 그려줘.

YouTube Data API를 사용하고,
API 키는 Streamlit Cloud의 Secrets 기능으로 안전하게 불러와줘.
main.py랑 requirements.txt 파일로 만들어줘.</div>

    <div class="fold-toggle" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')" style="margin-top:1rem">
      <div class="ft-left"><span class="ft-badge" style="background:var(--yt-bg);color:var(--yt)">RESULT</span><span class="ft-title">👀 Claude가 생성해준 코드 보기</span></div>
      <span class="ft-arrow">▶</span>
    </div>
    <div class="fold-body">
      <span class="code-label">main.py</span>
      <div class="code">
<span class="du">import</span> streamlit <span class="du">as</span> st
<span class="du">import</span> requests, pandas <span class="du">as</span> pd, plotly.express <span class="du">as</span> px

st.<span class="df">set_page_config</span>(page_title=<span class="ds">"YouTube 분석"</span>, page_icon=<span class="ds">"📺"</span>, layout=<span class="ds">"wide"</span>)
API_KEY = st.secrets[<span class="ds">"YOUTUBE_API_KEY"</span>]

query = st.<span class="df">text_input</span>(<span class="ds">"검색어"</span>, <span class="ds">"귀여운 고양이"</span>)
<span class="du">if</span> st.<span class="df">button</span>(<span class="ds">"🔍 검색"</span>):
    data = requests.<span class="df">get</span>(
        <span class="ds">"https://www.googleapis.com/youtube/v3/search"</span>,
        params={<span class="dk">"q"</span>: query, <span class="dk">"type"</span>: <span class="ds">"video"</span>,
                <span class="dk">"part"</span>: <span class="ds">"snippet"</span>,
                <span class="dk">"maxResults"</span>: <span class="dn">10</span>, <span class="dk">"key"</span>: API_KEY}
    ).<span class="df">json</span>()

    videos = []
    <span class="du">for</span> item <span class="du">in</span> data[<span class="ds">"items"</span>]:
        videos.append({
            <span class="ds">"제목"</span>: item[<span class="ds">"snippet"</span>][<span class="ds">"title"</span>],
            <span class="ds">"채널"</span>: item[<span class="ds">"snippet"</span>][<span class="ds">"channelTitle"</span>]
        })

    df = pd.<span class="df">DataFrame</span>(videos)
    st.<span class="df">dataframe</span>(df)</div>
      <span class="code-label">requirements.txt</span>
      <div class="code">streamlit
requests
pandas
plotly</div>
    </div>
  </div>

  <!-- Claude Prompt -->
  <div class="card" style="border-left:4px solid var(--cl)">
    <h3 style="font-size:1rem;margin-bottom:0.5rem">🤖 Claude AI 앱 — 프롬프트 예시</h3>
    <p style="font-size:0.78rem;color:var(--dim);margin-bottom:0.8rem">💬 이렇게 Claude에게 말해보세요:</p>
    <div class="code" id="prompt-cl" style="background:#fef9ee;color:#92400e;border:2px solid var(--cl);font-size:0.82rem;line-height:2"><button class="copy-btn" onclick="copyPrompt('prompt-cl')">📋 복사</button>Streamlit Cloud에 배포할 웹앱을 만들어줘.

Claude API로 AI한테 질문하는 앱이야.
AI 모델은 소넷 4.6 버전과 오퍼스 4.6 버전 중에
골라서 사용할 수 있게 해줘.

질문을 입력하면 AI가 답변해주고,
AI가 얼마나 사용했는지(입력/출력 사용량)도 보여줘.
API 키는 Streamlit Cloud의 Secrets 기능으로 안전하게 불러와줘.
main.py랑 requirements.txt 파일로 만들어줘.</div>

    <div class="fold-toggle" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')" style="margin-top:1rem">
      <div class="ft-left"><span class="ft-badge" style="background:var(--cl-bg);color:var(--cl)">RESULT</span><span class="ft-title">👀 Claude가 생성해준 코드 보기</span></div>
      <span class="ft-arrow">▶</span>
    </div>
    <div class="fold-body">
      <span class="code-label">main.py</span>
      <div class="code">
<span class="du">import</span> streamlit <span class="du">as</span> st
<span class="du">import</span> anthropic

st.<span class="df">set_page_config</span>(page_title=<span class="ds">"AI 도우미"</span>, page_icon=<span class="ds">"🤖"</span>)
client = anthropic.<span class="df">Anthropic</span>(
    api_key=st.secrets[<span class="ds">"ANTHROPIC_API_KEY"</span>]
)

model = st.<span class="df">selectbox</span>(<span class="ds">"AI 모델"</span>, [
    <span class="ds">"claude-sonnet-4-6"</span>,  <span class="dc"># 빠르고 저렴</span>
    <span class="ds">"claude-opus-4-6"</span>     <span class="dc"># 더 똑똑</span>
])

question = st.<span class="df">text_area</span>(<span class="ds">"질문을 입력하세요"</span>)
<span class="du">if</span> st.<span class="df">button</span>(<span class="ds">"🚀 질문하기"</span>) <span class="du">and</span> question:
    <span class="du">with</span> st.<span class="df">spinner</span>(<span class="ds">"AI가 생각하는 중..."</span>):
        msg = client.messages.<span class="df">create</span>(
            model=model,
            max_tokens=<span class="dn">1024</span>,
            messages=[{
                <span class="ds">"role"</span>: <span class="ds">"user"</span>,
                <span class="ds">"content"</span>: question
            }]
        )
        st.<span class="df">markdown</span>(msg.content[<span class="dn">0</span>].text)
        st.<span class="df">caption</span>(
            <span class="ds">f"입력: {msg.usage.input_tokens}토큰 / 출력: {msg.usage.output_tokens}토큰"</span>
        )</div>
      <span class="code-label">requirements.txt</span>
      <div class="code">streamlit
anthropic</div>
    </div>
  </div>

  <!-- Deployment -->
  <div class="card" style="background:var(--green-bg);border-color:rgba(16,185,129,0.2)">
    <h3 style="font-size:0.95rem;margin-bottom:0.8rem">🚀 배포 순서</h3>
    <div style="display:flex;flex-direction:column;gap:0.6rem;font-size:0.85rem;color:var(--dim)">
      <div style="display:flex;gap:0.6rem;align-items:flex-start"><span style="background:var(--green);color:white;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:700;flex-shrink:0">1</span><div><strong style="color:var(--text)">Claude에게 프롬프트 주기</strong> → main.py, requirements.txt 생성</div></div>
      <div style="display:flex;gap:0.6rem;align-items:flex-start"><span style="background:var(--green);color:white;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:700;flex-shrink:0">2</span><div><strong style="color:var(--text)">GitHub 저장소에 업로드</strong> (Public 저장소)</div></div>
      <div style="display:flex;gap:0.6rem;align-items:flex-start"><span style="background:var(--green);color:white;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:700;flex-shrink:0">3</span><div><strong style="color:var(--text)">Streamlit Cloud에 배포</strong> → share.streamlit.io에서 연결</div></div>
      <div style="display:flex;gap:0.6rem;align-items:flex-start"><span style="background:var(--green);color:white;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:700;flex-shrink:0">4</span><div><strong style="color:var(--text)">Secrets에 API 키 입력</strong> <strong style="color:var(--red)">← 코드에 직접 적으면 안 됨!</strong></div></div>
    </div>
    <div class="code" style="margin-top:1rem">
<span class="dc"># Streamlit Cloud → Settings → Secrets</span>
YOUTUBE_API_KEY = <span class="ds">"여러분의_유튜브_키"</span>
ANTHROPIC_API_KEY = <span class="ds">"여러분의_클로드_키"</span></div>
  </div>
</section>

<!-- ══════════════════════════════════════════ -->
<!-- SECTION 6: 퀴즈                            -->
<!-- ══════════════════════════════════════════ -->
<section class="sec" id="quiz">
  <span class="sec-label lb-quiz">SECTION 06</span>
  <h2>개념 확인 퀴즈</h2>
  <p class="lead">배운 내용을 얼마나 이해했는지 확인해보세요!</p>
  <div class="quiz-box">
    <div class="quiz-q" id="qz-q"></div>
    <div class="quiz-opts" id="qz-opts"></div>
    <div class="quiz-fb" id="qz-fb"></div>
    <div class="quiz-nav">
      <div class="quiz-score" id="qz-score"></div>
      <button class="sc-btn sc-primary" id="qz-next" onclick="nextQuiz()" style="display:none">다음 문제 →</button>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <p>당곡고/수도여고 인공지능과 피지컬 컴퓨팅 수업</p>
  <p style="margin-top:0.3rem">석리송 선생님의 API 특강! with claude ✨</p>
</footer>

<script>
/* ── Copy Prompt ── */
function copyPrompt(id){
  const el=document.getElementById(id);
  const text=el.textContent.replace('📋 복사','').trim();
  navigator.clipboard.writeText(text).then(()=>{
    const btn=el.querySelector('.copy-btn');
    btn.textContent='✅ 복사됨!';
    setTimeout(()=>{btn.textContent='📋 복사'},1500);
  });
}

/* ── Sequence Diagram Carousel ── */
const st8 = {yt:0, cl:0};
function getSteps(s){return document.querySelectorAll(`[data-scene="${s}"]`)}

function updateEntities(s, step){
  ['ec','ea','es'].forEach(k=>{
    const el=document.getElementById(s+'-'+k);
    if(el) el.classList.remove('active');
  });
  if(!step) return;
  const who=step.getAttribute('data-who')||'';
  if(who.includes('c')){const e=document.getElementById(s+'-ec');if(e)e.classList.add('active')}
  if(who.includes('a')){const e=document.getElementById(s+'-ea');if(e)e.classList.add('active')}
  if(who.includes('s')){const e=document.getElementById(s+'-es');if(e)e.classList.add('active')}
}

function resetScene(s){
  st8[s]=0;
  const box=getSteps(s)[0]?.closest('.scene-box');
  if(box) box.classList.remove('timeline');
  getSteps(s).forEach(e=>e.classList.remove('current'));
  document.getElementById('cnt-'+s).textContent=`0 / ${getSteps(s).length}`;
  updateEntities(s, null);
  const btn=document.getElementById('btn-'+s);
  btn.textContent='다음 단계 →';
  btn.onclick=function(){nextStep(s)};
}
function nextStep(s){
  const steps=getSteps(s);
  if(st8[s]>=steps.length) return;
  steps.forEach(e=>e.classList.remove('current'));
  steps[st8[s]].classList.add('current');
  updateEntities(s, steps[st8[s]]);
  st8[s]++;
  document.getElementById('cnt-'+s).textContent=`${st8[s]} / ${steps.length}`;
  steps[st8[s]-1].scrollIntoView({behavior:'smooth',block:'center'});
  if(st8[s]>=steps.length){
    const btn=document.getElementById('btn-'+s);
    btn.textContent='📋 전체 과정 한눈에 보기';
    btn.onclick=function(){
      const box=steps[0].closest('.scene-box');
      box.classList.add('timeline');
      updateEntities(s, null);
      box.scrollIntoView({behavior:'smooth',block:'start'});
      btn.textContent='처음으로';
      btn.onclick=function(){resetScene(s)};
    };
  }
}
function prevStep(s){
  if(st8[s]<=1) return;
  const steps=getSteps(s);
  const box=steps[0]?.closest('.scene-box');
  if(box) box.classList.remove('timeline');
  steps.forEach(e=>e.classList.remove('current'));
  st8[s]-=2;
  steps[st8[s]].classList.add('current');
  updateEntities(s, steps[st8[s]]);
  st8[s]++;
  document.getElementById('cnt-'+s).textContent=`${st8[s]} / ${steps.length}`;
  const btn=document.getElementById('btn-'+s);
  btn.textContent='다음 단계 →';
  btn.onclick=function(){nextStep(s)};
}

/* ── Quiz ── */
const quizzes=[
  {q:'API란 무엇일까요?',opts:['인터넷 브라우저의 종류','프로그램끼리 대화하는 규칙','파이썬 라이브러리 이름','데이터를 저장하는 장소'],a:1,ex:'API(Application Programming Interface)는 프로그램끼리 데이터를 주고받기 위한 규칙입니다!'},
  {q:'API Key를 코드에 직접 적으면 안 되는 이유는?',opts:['코드가 느려져서','GitHub에 노출될 수 있어서','API가 안 돌아가서','파이썬 문법 오류가 나서'],a:1,ex:'GitHub에 올리면 전 세계 누구나 키를 볼 수 있어요. 반드시 Secrets를 사용하세요!'}
];
let qi=0,qs=0,qa=false;
function renderQuiz(){const q=quizzes[qi];document.getElementById('qz-q').textContent=`Q${qi+1}. ${q.q}`;const c=document.getElementById('qz-opts');c.innerHTML='';q.opts.forEach((o,i)=>{const d=document.createElement('div');d.className='quiz-opt';d.textContent=o;d.onclick=()=>checkAns(i,d);c.appendChild(d)});document.getElementById('qz-fb').style.display='none';document.getElementById('qz-next').style.display='none';qa=false}
function checkAns(i,el){if(qa)return;qa=true;const q=quizzes[qi],opts=document.querySelectorAll('.quiz-opt');if(i===q.a){el.classList.add('correct');qs++}else{el.classList.add('wrong');opts[q.a].classList.add('correct')}const fb=document.getElementById('qz-fb');fb.textContent=(i===q.a?'✅ 정답! ':'❌ 틀렸습니다! ')+q.ex;fb.style.display='block';fb.style.background=i===q.a?'var(--green-bg)':'rgba(239,68,68,0.04)';fb.style.border=`1px solid ${i===q.a?'rgba(16,185,129,0.2)':'rgba(239,68,68,0.15)'}`;fb.style.color=i===q.a?'#059669':'#dc2626';document.getElementById('qz-score').textContent=`점수: ${qs}/${quizzes.length}`;document.getElementById('qz-next').style.display='inline-block';if(qi>=quizzes.length-1)document.getElementById('qz-next').textContent='결과 보기'}
function nextQuiz(){qi++;if(qi>=quizzes.length){document.getElementById('qz-q').textContent=`🎉 퀴즈 완료! ${qs}/${quizzes.length}점`;document.getElementById('qz-opts').innerHTML=qs===quizzes.length?'<p style="text-align:center;padding:1.5rem;color:#059669;font-size:1rem">완벽합니다! API 개념 완전 정복! 🏆</p>':'<p style="text-align:center;padding:1.5rem;color:var(--cl);font-size:1rem">잘했어요! 틀린 문제는 위 내용을 복습해보세요 📖</p>';document.getElementById('qz-fb').style.display='none';const b=document.getElementById('qz-next');b.textContent='다시 풀기';b.onclick=()=>{qi=0;qs=0;b.textContent='다음 문제 →';b.onclick=nextQuiz;document.getElementById('qz-score').textContent='';renderQuiz()};return}renderQuiz()}
renderQuiz();
</script>
</body>
</html>
