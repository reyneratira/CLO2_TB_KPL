namespace SimulasiProsesLayanan
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ServiceQueue queue = new ServiceQueue();
            queue.AddCustomer(new Customer("Alvin"));
            queue.AddCustomer(new Customer("Ilham"));
            queue.AddCustomer(new Customer("Reyner"));
            queue.AddCustomer(new Customer("Aulia"));

            queue.ShowQueue();
            queue.ProcessNext();
            queue.ProcessNext();
            queue.ProcessNext();
            queue.ProcessNext();
            queue.ProcessNext();
        }
    }
}
