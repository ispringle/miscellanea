import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig((configEnv) => {
  return {
    plugins: [
      configEnv.mode === 'development'
        ? undefined
        : viteStaticCopy({
            targets: [
              {
                src: 'src/day/',
                dest: './src/',
              },
            ],
          }),
    ],
  };
});
