import {
  ModuleRegistry,
  AllCommunityModule,
  createGrid,
  themeAlpine,
  themeBalham,
  themeMaterial,
  themeQuartz,
  colorSchemeVariable,
} from "ag-grid-community";
import { AllEnterpriseModule, LicenseManager, IntegratedChartsModule } from "ag-grid-enterprise";
import { AgChartsEnterpriseModule } from "ag-charts-enterprise";

ModuleRegistry.registerModules([
  AllCommunityModule,
  AllEnterpriseModule,
  IntegratedChartsModule.with(AgChartsEnterpriseModule),
]);

export default {
  createGrid,
  LicenseManager,
  themes: {
    alpine: themeAlpine,
    balham: themeBalham,
    material: themeMaterial,
    quartz: themeQuartz,
  },
  colorSchemeVariable,
};
