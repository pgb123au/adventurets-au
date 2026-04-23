// Data loaded from JSON files (editable via Decap CMS at /admin/)
import settingsData from './settings.json';
import servicesData from './services.json';
import teamData from './team.json';
import homepageData from './homepage.json';

export const site = settingsData as typeof settingsData;
export const team = teamData.items;
export const services = servicesData.items;
export const homepage = homepageData;

export const values = [
  { name: "Create Stability", icon: "/images/values/create-stability.png" },
  { name: "Be Curious", icon: "/images/values/be-curious.png" },
  { name: "Choose Quality over Quantity", icon: "/images/values/choose-quality.png" },
  { name: "Take Action", icon: "/images/values/take-action.png" },
  { name: "Support Flexibility", icon: "/images/values/be-versatile.png" },
] as const;

export const whoWeWorkWith = homepage.whoWeWorkWith.map(w => w.name);

export const navLinks = [
  { label: "Home", href: "/" },
  { label: "Services", href: "/services/", children: services.map(s => ({ label: s.name, href: `/services/${s.slug}/` })) },
  { label: "Team", href: "/team/" },
  { label: "FAQs", href: "/faqs/" },
  { label: "Contact", href: "/contact/" },
] as const;
