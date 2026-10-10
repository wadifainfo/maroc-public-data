// Moroccan public holidays, school breaks, civil-service concours and salaries from the free Wadifa Info API.
// No key, no dependencies (uses fetch). Data licence CC BY 4.0: show "Source : Wadifa Info" with a link.
// Docs: https://www.wadifa-info.com/developpeurs
const BASE = "https://www.wadifa-info.com/api/v1/";
const get = async (path) => (await fetch(BASE + path)).json();

export const holidays = async (year) =>
  (await get("jours-feries")).holidays.filter((h) => !year || h.date.startsWith(String(year)));
export const isHoliday = async (day) => {
  const d = day instanceof Date ? day.toISOString().slice(0, 10) : String(day).slice(0, 10);
  return (await holidays()).some((h) => h.date === d);
};
export const schoolBreaks = async () => (await get("vacances-scolaires")).breaks;
export const concours = async (lang = "fr", limit = 100) => (await get(`concours?lang=${lang}&limit=${limit}`)).items;
export const salaries = async () => (await get("salaires")).items;
