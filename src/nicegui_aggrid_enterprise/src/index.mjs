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
import { AllEnterpriseModule, LicenseManager } from "ag-grid-enterprise";

ModuleRegistry.registerModules([AllCommunityModule, AllEnterpriseModule]);

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
