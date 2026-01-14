import nodeResolve from "@rollup/plugin-node-resolve";
import terser from "@rollup/plugin-terser";

const commonPlugins = [
  nodeResolve(),
  terser({
    mangle: true,
  }),
];

export default [
  // Community charts bundle (AgGridEnterprise)
  {
    input: "./src/index.mjs",
    output: {
      file: "./dist/index.js",
      format: "es",
      sourcemap: true,
    },
    plugins: commonPlugins,
  },
  // Enterprise charts bundle (AgGridEnterpriseCharts)
  {
    input: "./src/index-enterprise-charts.mjs",
    output: {
      file: "./dist-enterprise-charts/index.js",
      format: "es",
      sourcemap: true,
    },
    plugins: commonPlugins,
  },
];
