import Image from "next/image";

const capabilities = [
  "Automatizaciones inteligentes",
  "Agentes IA personalizados",
  "Desarrollo web a medida",
  "Optimizacion de procesos",
];

const processSteps = [
  {
    number: "01",
    title: "Diagnostico",
    body: "Detectamos oportunidades, friccion y datos clave antes de construir.",
  },
  {
    number: "02",
    title: "Diseno del sistema",
    body: "Definimos flujos, agentes, integraciones y criterios de exito.",
  },
  {
    number: "03",
    title: "Implementacion",
    body: "Construimos, conectamos y probamos la operacion completa.",
  },
  {
    number: "04",
    title: "Optimizacion",
    body: "Medimos, mejoramos y escalamos lo que genera resultados.",
  },
];

export default function Home() {
  return (
    <main className="aetria-page">
      <header className="aetria-nav">
        <Image
          src="/brand/logo_navbar_600x180_transparent.png"
          alt="AETRIA STUDIOS"
          width={600}
          height={180}
          priority
        />
        <a href="https://wa.me/56968171774?text=Hola%20AETRIA%20STUDIOS%2C%20quiero%20agendar%20una%20llamada">
          Agenda una llamada
        </a>
      </header>

      <section className="next-hero">
        <div className="neural-lines" aria-hidden="true">
          <span />
          <span />
          <span />
        </div>
        <div className="next-hero-copy">
          <Image
            src="/brand/logo_web_header_1200x360_transparent.png"
            alt="AETRIA STUDIOS"
            width={1200}
            height={360}
            priority
            className="next-wordmark"
          />
          <p className="next-eyebrow">Automatizacion · IA · Desarrollo</p>
          <h1>Sistemas de IA que trabajan por tu negocio.</h1>
          <p>
            Creamos soluciones inteligentes que automatizan procesos, ahorran
            tiempo y multiplican resultados.
          </p>
          <div className="next-actions">
            <a href="https://wa.me/56968171774?text=Hola%20AETRIA%20STUDIOS%2C%20quiero%20agendar%20una%20llamada">
              Agenda una llamada
            </a>
            <a href="#proceso">Ver proceso</a>
          </div>
          <div className="capability-row">
            {capabilities.map((item) => (
              <span key={item}>{item}</span>
            ))}
          </div>
        </div>

        <div className="dashboard-card" aria-label="Vista conceptual de dashboard IA">
          <div className="dashboard-head">
            <span>Dashboard</span>
            <strong>AETRIA</strong>
          </div>
          <div className="dashboard-kpis">
            <div><span>Procesos</span><strong>24</strong></div>
            <div><span>Horas</span><strong>320+</strong></div>
            <div><span>Tareas</span><strong>12.458</strong></div>
            <div><span>Eficiencia</span><strong>98%</strong></div>
          </div>
          <svg viewBox="0 0 520 180" className="next-chart" aria-hidden="true">
            <path d="M20 140 L70 104 L118 128 L168 70 L220 88 L270 45 L322 103 L374 84 L424 96 L476 52 L505 36" />
          </svg>
          <div className="agent-list">
            <span>Agente de ventas <strong>Activo</strong></span>
            <span>Agente de soporte <strong>Activo</strong></span>
            <span>Agente de contenido <strong>Activo</strong></span>
          </div>
        </div>
      </section>

      <section id="proceso" className="next-process">
        <p className="next-eyebrow">Nuestro proceso</p>
        <h2>De la idea a resultados reales.</h2>
        <div className="process-grid">
          {processSteps.map((step) => (
            <article key={step.number}>
              <div className="orb">{step.number}</div>
              <h3>{step.title}</h3>
              <p>{step.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="next-map">
        <Image
          src="/brand/ai_process_background_banner_1920x700.png"
          alt="Mapa de automatizacion inteligente AETRIA"
          width={1920}
          height={700}
        />
        <div>
          <p className="next-eyebrow">Mapa IA</p>
          <h2>Datos, procesos y personas conectados a un nucleo inteligente.</h2>
        </div>
      </section>
    </main>
  );
}
