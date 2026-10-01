from pathlib import Path
ROOT = Path(__file__).parent
parts = [ROOT/'userscript.meta.js', ROOT/'src/core.js', ROOT/'src/connectors/_stub_factory.js']
for name in ['facebook','bluesky','youtube','tiktok','kick','twitch','discord','instagram','threads','pinterest','kwai','x','whatsapp','github','telegram']:
    parts.append(ROOT/f'src/connectors/{name}.js')
parts += [ROOT/'src/ui.js', ROOT/'src/main.js']
out = ROOT/'dist/social-hub.user.js'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text('\n\n'.join(p.read_text(encoding='utf-8-sig') for p in parts), encoding='utf-8')
print(out)
